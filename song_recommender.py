import matplotlib
matplotlib.use('Agg')

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master = None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

    def create_widgets(self):
            self.recommender = tk.Button(self)
            self.recommender["text"] = "Get Recommendation"
            self.recommender["command"] = self.run_recommender
            self.recommender.pack(side="bottom")

            self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)
            self.quit.pack(side="bottom")
    
    def run_recommender(self):
        # print("Pass")
        pass


root = tk.Tk()
app = Application(master = root)
app.mainloop()

# window
#   - file browser, "go" button
#   - recommendation 

