import tkinter as tk

class Main_Menu(tk.Frame):
    def __init__(self, parent, myframe):
        tk.Frame.__init__(self, parent)
        self.myframe = myframe

        self.topframe = tk.Frame(self, bg="white", height=600, width=900)
        self.topframe.place(x=0, y=0)

        self.myframe.background_image(self.topframe)

        title = tk.Label(self.topframe, text="HANGMAN", font=("Comic Sans Ms", 80, "italic"), bg="white")
        title.place(x=170, y=10)

        newgame = tk.Button(self.topframe, text="NEW GAME", bg="light gray", font=("Comic Sans Ms", 20), command=lambda:(self.myframe.play_sound("click"), self.myframe.change_frame("Category")))
        newgame.place(x=370, y=350)
        mechanics = tk.Button(self.topframe, text="MECHANICS", bg="light gray", font=("Comic Sans Ms", 20), command=lambda:(self.myframe.play_sound("click"), self.myframe.change_frame("Mechanics")))
        mechanics.place(x=360, y=450)
