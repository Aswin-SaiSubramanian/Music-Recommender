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
            self.status = False
            self.create_widgets()
            self.Recommendation_System = rec()
            self.name_of_target_file = ""
            
    def enable(self, x):
        x.config(state=tk.NORMAL)
        
    def disable(self, x):
        x.config(state=tk.DISABLED)
    
    
    def create_widgets(self):
            self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)
            self.quit.pack(side=tk.RIGHT, pady = 5, padx = 5)

            self.text = tk.Text(self.master)
            self.text.pack(side=tk.BOTTOM)
            self.disable(self.text)

            self.browse = tk.Button(self)
            self.browse["text"] = "Browse..."
            self.browse["command"] = self.file_browser
            self.browse.pack(side=tk.LEFT, pady = 5, padx = 5)

            self.recommender = tk.Button(self)
            self.recommender["text"] = "Get Recommendation"
            self.recommender["command"] = self.run_recommender
            self.recommender.pack(side=tk.TOP, pady = 5, padx = 5)
            

            
    def file_browser(self):
            self.file = tk.filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            if self.file:
                self.status = True
                self.name_of_target_file = self.file.name
                self.name_of_target_file = self.name_of_target_file.split('/')[-1]
                self.file.close()
                
                self.enable(self.text)
                self.text.delete('1.0', tk.END) 
                self.text.insert(tk.INSERT, "Success") # for testing
                self.disable(self.text)
                
                self.enable(self.recommender)
                self.disable(self.browse)

            else:
                self.status = False
                self.disable(self.recommender)
                
                self.enable(self.text)
                self.text.insert(tk.INSERT, "File is not available.") # for testing
                self.disable(self.text)

    def run_recommender(self):
            if self.status:
                imgs = self.Recommendation_System.get_3channel_spectrograms(self.name_of_target_file)
                # Run the recommender
                genre = self.Recommendation_System.get_genre_prediction(imgs)
                result = self.Recommendation_System.get_recommendation(genre)

                self.enable(self.text)
                disp_string = "You might also like: " + result
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.INSERT, disp_string) # for testing
                self.disable(self.text)

                self.enable(self.browse)
            else:
                self.enable(self.text)
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.INSERT, "Please select an audio file.") # for testing
                self.disable(self.text)
        


root = tk.Tk()
root.geometry("600x400")
app = Application(master = root)
app.mainloop()

