# Generate Spectrograms

#pip install youtube_dl
#pip install pydub
#wget https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/PythonSrc/hdf5_getters.py
#pip install tables # need PyTables package to use hdf5_getters
#pip install pickle-mixin

# importsimport librosa
import librosa.display
import IPython.display as ipd
import wave # to find the duration of a song
import youtube_dl
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import torch, torchvision
import os
import statistics
import random
import tables
import pickle

from torch import nn, optim
from torchvision import datasets, models, transforms
from google_drive_downloader import GoogleDriveDownloader as gdd
from torch.autograd import Variable

class Recommender(): 

    def __init__(self):

        # get the saved parameters of the VGG-19 from Google Drive 
        gdd.download_file_from_google_drive(file_id='1zwbum2Bq9VuVnwS0c239bIKqgpEj163r',
                                            dest_path='./cpen291_proj_genreClassifier.zip',
                                            unzip=True)

        self.loaded_model = models.vgg19(pretrained=True)

        # change last layer of the model to have 8 outputs instead of 1000
        self.loaded_model.classifier = nn.Sequential(
            nn.Linear(in_features=25088, out_features=4096, bias=True), 
            nn.ReLU(inplace=True), 
            nn.Dropout(p=0.5, inplace=False), 
            nn.Linear(in_features=4096, out_features=4096, bias=True), 
            nn.ReLU(inplace=True), 
            nn.Dropout(p=0.5, inplace=False), 
            nn.Linear(in_features=4096, out_features=8, bias=True)
        )

        self.loaded_model.load_state_dict(torch.load("./cpen291_proj_genreClassifier.pt", map_location=torch.device('cpu')))
        self.loaded_model.eval()

    # Visualizing the spectrogram
    def plot_spectrogram(self, Y, sr=22050, hop_length=2965, y_axis="linear"):
      fig = plt.figure(figsize=(25,10))
      # plt.axis('off')
      librosa.display.specshow(
          Y,
          sr=sr,
          hop_length=hop_length,
          x_axis="time",
          y_axis=y_axis
      )
      plt.colorbar(format="%+2.f")
      return fig

    # find the number of spectrograms that can be generated from an audio file
    def __num_spectrograms_possible__(self, song_file):
      read = wave.open(song_file)
      framerate = read.getframerate() # get sample rate
      numframes = read.getnframes()   # get number of samples
      duration = numframes/framerate  # duration of song: frames/frames-per-second = seconds
      read.close()
      # print(duration)
    
      # compute the number of 90 second clips available in this file
      num_spectrograms = int(duration / 90)
      return num_spectrograms

    # Returns a 2-d array containing 90-second clips from a wav file in 3 chunks of 30 each.
    # Each chunk corresponds to one channel of a spectrogram to be fed into VGG-19 
    def __get_song_clips__(self, song_file):
      audio = AudioSegment.from_wav(song_file)
      song_files = [] 
      for j in range(self.__num_spectrograms_possible__(song_file)):
        clips = []
        for i in range(3):
          t1 = (j*90*1000) + (i*30) * 1000 #Works in milliseconds
          t2 = (j*90*1000) + (i*30 + 30) * 1000
          newAudio = audio[t1:t2]
          newAudio.export(f'{j*90 + i*30}to{j*90 + i*30 + 30}-' + song_file, format="wav") #Exports to a wav file in the current path.
          clips.append(f'{j*90 + i*30}to{j*90 + i*30 + 30}-' + song_file)
        song_files.append(clips)
      return song_files


    # Loads audio files from __get_song_clips__() into librosa.
    # Returns a numpy array representing those clips. 
    def __librosa_load_song_clips__(self, song_files):
      song_clips = []
      for clips in song_files:
        song_chunks = []
        for chunks in clips:
          song, sr = librosa.load(chunks)
          song_chunks.append(song)
          # print(sr)
        song_clips.append(song_chunks)
      return song_clips

    # Takes as input, the output of __librosa_load_song_clips__() (2-d array of numpy arrays 
    # representing 90-second song clips, each split into 3 separate numpy arrays, 
    # all loaded into librosa). Returns an numpy array with same shape as the input,  
    # containing the stft (short time fourier transform) of each element in the input array.
    def __get_stft_of_clips__(self, song_clips):
      # extracting short-time fourier transform
      FRAME_SIZE = 446 # frame size chosen such that frequency_bins = frame_size/2 - 1 = 224
      HOP_SIZE = 2965  # Hop size chosen such that num_frames = (samples - frame_size)/ hop_size + 1 = 224 
                       # Output shape of the stft is (frequency_bins, num_frames). Desired: (224, 224)
      stft = []
      for i in range(len(song_clips)):
        channels = []
        for j in range(len(song_clips[i])):
          channels.append(librosa.stft(song_clips[i][j], n_fft=FRAME_SIZE, hop_length=HOP_SIZE))
        stft.append(channels)
      return stft

    # Calculates and returns the spectrograms of each element in the input numpy array 
    # (in a numpy array with the same shape as the input array). I.e. converts the elements 
    # of the input array from complex valued arrays to float arrays. 
    # The input numpy array must be the output of __get_stft_of_clips__().
    def __calculate_spectrograms__(self, stft):
      specs = []
      for i in range(len(stft)):
        channels = []
        for j in range(len(stft[i])):
          channels.append(np.abs(stft[i][j]) ** 2)
        specs.append(channels)
      return specs


    # compute and return the log-amplitude spectrograms for the spectrograms created 
    # by __calculate_spectrogram__().
    def __log_amplitude_transform__(self, specs):
      log_specs = []
      for i in range(len(specs)):
        channels = []
        for j in range(len(specs[i])):
          log_converted_spec = librosa.power_to_db(specs[i][j])
          channels.append(log_converted_spec)
        log_specs.append(channels)
      return log_specs

    # Takes as its input (log_specs), the output of __log_amplitude_transform__(). 
    # This function transforms log_specs[i][:] into tensors of size (3 x 224 x 224)
    def __log_specs_to_image_tensors__(self, log_specs):
      imgs = []
      for i in range(len(log_specs)):
        img = torch.tensor(log_specs[i])
        imgs.append(img)
      return imgs

    # a function to delete all intermediate wav files
    def __remove_intermediate_wav_files__(self, song_file):
      j = 0
      i = 0
      for j in range(self.__num_spectrograms_possible__(song_file)):
        for i in range(3):
          os.remove(f'{j*90 + i*30}to{j*90 + i*30 + 30}-' + song_file)


    # Putting everything together: The Spectrogram Extraction Process

    # A funtion that takes in the name of a song file (that is assumed to exist), 
    # and returns a list of spectrograms of size (3 x 224 x 224) 
    def get_3channel_spectrograms(self, song_file):
      # get 90-second song clips, in three 30-second chunks each
      file_names = self.__get_song_clips__(song_file)
      # load song clips to librosa
      song_clips = self.__librosa_load_song_clips__(file_names)
      # calculate stft's of each clip
      stft = self.__get_stft_of_clips__(song_clips)
      # calculate spectrograms based on stft's
      specs = self.__calculate_spectrograms__(stft)
      # transform spectrograms to log-amplitude
      log_specs = self.__log_amplitude_transform__(specs)
      # create 3-channel image tensors from each set of 3 spectrograms in log_specs
      imgs = self.__log_specs_to_image_tensors__(log_specs)
      # remove intermediate wave files
      self.__remove_intermediate_wav_files__(song_file) 
      return imgs

##########################################################################

    def get_genre_prediction(self, imgs):
        
      # getting the predictions for each 3-channel spectrograms. Stored in resuts
      results = []
      for x in imgs:
        model_input = x.unsqueeze(dim=0)
        r = self.loaded_model(model_input.to(torch.device('cpu')))
        _, r = torch.max(r.detach(), 1)
        results.append(r.squeeze())

      # get the sum of prediction made by the model (before finding mean)
      result_sum = 0
      for i in range (len(results)):
        result_sum += results[i]

      # get the mean of the predictions made by the model
      prediction = torch.round(result_sum / len(results))

      return prediction


    def get_recommendation(self, genre_label):
      # mapping from model's genre prediction to genre name
      # {0: "Electronic", 
      #  1: "Jazz", 
      #  2: "Rap", 
      #  3: "Rock", 
      #  4: "Latin", 
      #  5: "Folk", 
      #  6: "Blues", 
      #  7: "Country"}
      genre_label = int(genre_label) # converting a single-element tensor to int for translating into a genre name 
      genres = ["Electronic", "Jazz", "Rap", "Rock"]

      # Get the genre name from the model's prediction
      genre = genres[genre_label]

      # Dictionary that maps genre to song name and artist can be loaded from:
      # song_to_genre.pickle 

      song_to_genre = {}
      with open('./song_to_genre.pickle', 'rb') as handle:
          song_to_genre = pickle.load(handle)

      # Getting Identifying Information of Another Song in the Same Genre
      # - generate random number "index" in range(num_of_files_in_dir- 1)
      # - find the number of songs available for the desired genre in song_to_genre (num_songs_in_genre)
      # - Traverse through index % num_songs_in_genre elements of the desired genre in song_to_genre
      # The music recommendation is the element of song_to_genre that we stop at.

      # find the number of songs available in the dictionary song_to_genre, with the desired genre
      num_songs_in_genre = 0
      for x in song_to_genre:
        if song_to_genre[x] == genre:
          num_songs_in_genre += 1

      # Iterating through the song_to_genre dictionary to find a song recommendation for our output
      torch.manual_seed(291)
      np.random.seed(291)
      index = random.randint(0, num_songs_in_genre)
      count = 0
      recommendation = ""
      for song in song_to_genre:
        if song_to_genre[song] == genre:
          if count == index:
            recommendation = song
            break
          else:
            count += 1
            
      return recommendation