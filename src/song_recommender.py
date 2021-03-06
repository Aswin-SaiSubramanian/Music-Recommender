import matplotlib
matplotlib.use('Agg') 
import tkinter as tk
from tkinter import filedialog
from recommender import Recommender as rec
import time

class Application(tk.Frame):
    def __init__(self, master = None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.status = False                 # is set to True when an input wav file is selected
            self.create_widgets()
            self.Recommendation_System = rec()
            self.name_of_target_file = ""
            
    def enable(self, x):
        x.config(state=tk.NORMAL)
        
    def disable(self, x):
        x.config(state=tk.DISABLED)
    
    
    def create_widgets(self):
            
            # don't assume that self.parent is a root window.
            # instead, call `winfo_toplevel to get the root window
            # (https://stackoverflow.com/questions/2395431/using-tkinter-in-python-to-edit-the-title-bar)
            self.winfo_toplevel().title("Parasaurolophus: Music Recommender")

            # Adding GUI components...
            
            HOR_PAD = 25
            VERT_PAD = 25 

            # ...a button to exit the program
            self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)
            self.quit.pack(side=tk.RIGHT, pady = VERT_PAD, padx = HOR_PAD)

            # ... a text box in which the application displays its outputs instead of command line
            self.text = tk.Text(self.master)
            self.text.pack(side=tk.BOTTOM, pady = 5, padx = 5)
            self.text.insert(tk.INSERT, "Welcome to the parasaurolophus' home! \nPlease show me an example of a song you like (wav file, please).") 
            self.disable(self.text)

            # ... a button to tell the app to open a file browser (for selecting a wav file as the app's input)
            self.browse = tk.Button(self)
            self.browse["text"] = "Browse..."                       # setting display text
            self.browse["command"] = self.file_browser              # setting button's function
            self.browse.pack(side=tk.LEFT, pady = VERT_PAD, padx = HOR_PAD)

            # ... a button to initiate the song recommendation process
            self.recommender = tk.Button(self)
            self.recommender["text"] = "Get Recommendation!"         # setting display text
            self.recommender["command"] = self.run_recommender      # setting button's function
            self.recommender.pack(side=tk.TOP, pady = VERT_PAD, padx = HOR_PAD)
            

            
    def file_browser(self):
            self.file = tk.filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            if self.file and self.file.name.split('.')[-1] == "wav":
                self.status = True                                  # Recording that an input wav file has been selected
                self.name_of_target_file = self.file.name           # Gets the path to the selected wav file
                # print(self.name_of_target_file.split('.')[-1])
                self.name_of_target_file = self.name_of_target_file.split('/')[-1]  # Extracts the name of the wav file from its path 
                self.file.close()
                
                # Writing feedback text to GUI
                self.enable(self.text)
                self.text.delete('1.0', tk.END) 
                self.text.insert(tk.INSERT, "Success! File found.") 
                self.disable(self.text)
                
                self.enable(self.recommender)
                self.disable(self.browse)                           # Have already selected an input file. Only need the "Get recommendation" button.
            
            else:
                self.status = False                                 # Ensures that self.status remains False when no input wav file is selected
                self.disable(self.recommender)
                
                # Writing feedback text to GUI
                self.enable(self.text)
                if self.file:
                    if (self.file.name.split('.')[-1] != "wav"):
                        self.text.delete('1.0', tk.END)
                        self.text.insert(tk.INSERT, "Invalid file extension. Please select a wav file.") 
                else:
                    self.text.delete('1.0', tk.END)
                    self.text.insert(tk.INSERT, "No file selected. Please select a wav file.") 
                self.disable(self.text)

    def run_recommender(self):
            if self.status:
                
                # Generate spectrograms from input wav file
                imgs = self.Recommendation_System.get_3channel_spectrograms(self.name_of_target_file)
                
                # Run the recommender
                genre = self.Recommendation_System.get_genre_prediction(imgs)
                result = self.Recommendation_System.get_recommendation(genre)

                # Writing music recommendation to GUI
                self.enable(self.text)
                disp_string = "Parasaurolophus recommends: " + result
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.INSERT, disp_string) 
                # copy recommendation to clipboard (referred to https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard)
                self.master.clipboard_clear()
                self.master.clipboard_append(result)
                self.master.update()                                # Allows output to persist on the clipboard after the window is closed
                self.text.insert(tk.INSERT, "\n...Recommendation copied to clipboard...")
                self.disable(self.text)

                self.enable(self.browse)                            # Re-enable "Browse" button to allow the user to select the next wav file to analyse
            else:
                # Writing feedback text to GUI
                self.enable(self.text)
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.INSERT, "Please select an audio file.") 
                self.disable(self.text)
        


root = tk.Tk()
root.geometry("600x150")
app = Application(master = root)
app.mainloop()

