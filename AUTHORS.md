# Contributors

- Aswin Sai Subramanian
- Cassiel Jung 
- Matthew Poon 
- Quinn Carroll

# Overall Contributions

Note: "M1," "M2," "M3," and "M4" refer the four milestones that the project was broken into.

**My Contributions**
- Sai Subramanian, Aswin
    - Helped improve the accuracy of our genre classifier from 40% to 60%: 
        - Experimented with model training parameters such as number of genres, number of samples per genre to find trends in training results. This helped make decisions about how to improve the genre classifier’s accuracy (M3/M4).
        - Merged additional spectrograms collected by team members into full dataset (M4).
        - Performed tests to determine an effective batch-size to speed up training time (M2). 
    - Layed the foundation for our genre classifier's training and testing datasets:
        - Developed spectrogram extraction process (M3).
        - Developed process to download audio samples from YouTube, and store spectrograms generated from them into our dataset (M3).
    - Debugged GUI functions with Matthew (M4). 
    - Made project demo video (demos/project_demo.mp4, M4).
    - Collected .h5 files for Rock and Jazz from the Million Song Dataset (M1).
    

**Team-mate Contributions**

<details>
<summary>Jung, Cassiel</summary>
<br>
- Collected .h5 file of Folk and Blues from the Million Song Dataset (M1)<br>
- Tested the model by differing the step size while keeping the other values constant to get the best accuracy (M2)<br>
- Wrote dataset class that matches spectrograms and genre with Quinn (M3)<br>
- Collected spectrograms to increase number of samples used for training model(M4)<br>
- Folk, Blues, Latin and Country<br>
- Made last GUI feedback to check if everything works fine (M4)<br>
</details> 

<details>
<summary>Poon, Matthew</summary>
<br>
- Created a script to extract and filter h5 song samples from the Million Song Dataset (M1)<br>
- Collected h5 files for Metal, Reggae, Classical, Latin, and Electronic music.(Metal, Reggae, and Classical discarded due to lack of samples) (M1)<br> 
- Created the structure used for storing the dataset (individual genre folders)(M2)<br>
- Performed tests to determine the best learning rate for our model (M2)<br>
- Created a script to extract information and save dictionaries for URL:Genre,TrackID:Genre, and Song:Genre (M3)<br>
- Debugged GUI functions with Aswin (M4)<br>
- Collected spectrograms for additional samples for following genres: Rap, Latin, Jazz, Electronic (M4)<br>
- Recorded and edited the project presentation video for final submission
</details>

<details>
<summary>Carroll, Quinn</summary>
<br>
- Collected h5 files of Rap and Country songs from the Million Song Dataset (M1)<br>
- Performed testing on the model to find the best values for gamma and momentum(M2)<br>
- Created class genreClassificationDatasetSpectrogram in paired programmingsession with Cassiel (M3)<br>
- Collected spectrograms from youtube audio to increase number of samples inBlues subset (M4)<br>
- Created data flow diagram of our genreClassifier process (M4)<br>
- Created outline for video presentation (M4)
</details>
 
**Shared Contributions (Paired Programming Style)**
- Created a custom dataset class that:
    - Extracts features found in h5 files in the Million Song Dataset (M2)
    - Takes these features and moulds them into the correct shape for the VGG model (M2)
- Developed the ML-model wrapper that prepares the model inputs from a wav file, feeds them into the model, interprets the results to classify the audio sample's music genre, and recommends another song of the same genre (genre_classifier_development/Recommender System M3.ipynb, M3).
- Created the class Recommender, which collects the functionality of the ML-model wrapper developed in M3 into a class which can be instantiated and used in our main app along with the GUI (src/recommender.py, M4).
- Created a GUI combining the different modules of the project (src/song_recommender.py, M4)
- Created the Google Slides presentation and recorded audio for the project presentation video. 

# Further Contribution Details
See the "Contributions" section towards the end of each milestone report:
- [Milestone 1 Report](https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M1/Team%20Dilphosaurus%20-%20Milestone%201%20Report.pdf)
- [Milestone 2 Report](https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M2/Team%20Dilphosaurus%20-%20Milestone%202%20Report.pdf)
- [Milestone 3 Report](https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M3/Team%20Dilphosaurus%20-%20Milestone%203%20Report.pdf)
- [Milestone 4 Report](https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M4/Team%20Dilphosaurus%20-%20Milestone%204%20Report.pdf)
  
