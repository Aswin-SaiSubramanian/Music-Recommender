import matplotlib
matplotlib.use('Agg')

import tkinter as tk
from tkinter import filedialog
from recommender import Recommender as rec

class Application(tk.Frame):
    def __init__(self, master = None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()
            self.Recommendation_System = rec()
            
    def enable(x):
        x.config(state=NORMAL)
        
    def disable(x):
        x.config(state=DISABLED)
    
    
    def create_widgets(self):
            self.recommender = tk.Button(self)
            self.recommender["text"] = "Get Recommendation"
            self.recommender["command"] = self.run_recommender
            self.recommender.pack(side="top")

            self.browse = tk.Button(self)
            self.browse["text"] = "Browse..."
            self.browse["command"] = self.file_browser
            self.recommender.pack(side="right")

            self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)
            self.quit.pack(side="bottom")

            # self.disable()

    def file_browser(self):
            self.file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            if self.file:
                data = file.read()
                file.close()
                print("Success") # for testing
                # self.enable(self.recommender)
            else:
                # self.disable(self.recommender)
                print("File not available.")

    def run_recommender(self):
            if self.file:
                imgs = get_3channel_spectrograms(self.file)
                # Run the recommender
                genre = Recommendation_System.get_genre_prediction(imgs)
                result = Recommendation_System.get_recommendation(genre)
                print("")
            else:
                print("Please select an audio file.")
        


root = tk.Tk()
root.geometry("600x400")
app = Application(master = root)
app.mainloop()

# window
#   - file browser, "go" button
#   - recommendation 