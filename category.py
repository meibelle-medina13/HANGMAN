import tkinter as tk

class Category(tk.Frame):

    def __init__(self, parent, myframe):
        tk.Frame.__init__(self, parent)
        self.myframe = myframe

        self.topframe = tk.Frame(self, bg="white", height=600, width=900)
        self.topframe.place(x=0, y=0)

        self.myframe.background_image(self.topframe)

        title = tk.Label(self.topframe, text="Categories", font=("Comic Sans Ms", 50), bg="white")
        title.place(x=290, y=30)

        self.choices()

    def choices(self):
        coun = tk.Button(self.topframe, text="Country", bg="light gray", font=("Comic Sans Ms", 30), command=lambda:(self.myframe.play_sound("click"), self.pass_category(0)))
        coun.place(x=90, y=200)

        fud = tk.Button(self.topframe, text="Food", bg="light gray", font=("Comic Sans Ms", 30), command=lambda:(self.myframe.play_sound("click"), self.pass_category(1)))
        fud.place(x=400, y=200)

        sp0rts = tk.Button(self.topframe, text="Sports", bg="light gray", font=("Comic Sans Ms", 30), command=lambda:(self.myframe.play_sound("click"), self.pass_category(2)))
        sp0rts.place(x=680, y=200)

        s_media = tk.Button(self.topframe, text="Social Media", bg="light gray", font=("Comic Sans Ms", 30), command=lambda:(self.myframe.play_sound("click"), self.pass_category(3)))
        s_media.place(x=320, y=350)

        exit = tk.Button(self.topframe, text="Exit", bg="light gray", font=("Comic Sans Ms", 15), width=10, command=lambda:(self.myframe.play_sound("click"), self.myframe.change_frame("Main_Menu")))
        exit.place(x=20, y=530)

    def pass_category(self, index_cat):
        self.myframe.subframes["Level"].buttons(index_cat)
        self.myframe.change_frame("Level")
