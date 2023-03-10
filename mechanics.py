import tkinter as tk
from PIL import Image, ImageTk

class Mechanics(tk.Frame):
    def __init__(self, parent, myframe):
        tk.Frame.__init__(self, parent)
        self.myframe = myframe

        self.topframe = tk.Frame(self, bg="white", height=600, width=900)
        self.topframe.place(x=0, y=0)

        title = tk.Label(self.topframe, text="MECHANICS", font=("Comic Sans Ms", 50), bg="white")
        title.place(x=250, y=30)

        image = Image.open("./resources/images/win.png")
        resize = image.resize((550, 200))
        img = ImageTk.PhotoImage(resize)

        image_label = tk.Label(self.topframe, bg="white", image=img)
        image_label.image = img
        image_label.place(x=220, y=425)

        mech_frame = tk.Frame(self.topframe, width=800, height=320, bg="white")
        mech_frame.place(x=50, y=130)

        text="1. Choose a category.\n2. Select your current level from your chosen category.\n3. Try to guess a letter.\n4. Correct letter will fill its designated blank in screen.\n5. Wrong letter will be grayed out and will \nput a man closer to being hanged.\n6. Once you've guessed all the correct letters, \nyou will win the game, otherwise, a man will be a hanged!"

        mech_label = tk.Label(mech_frame, text=text, font=("Comic Sans Ms", 20), bg="white")
        mech_label.place(x=50, y=0)

        back = tk.Button(self.topframe, text="Back", bg="light gray", font=("Comic Sans Ms", 15), width=10, command=lambda:(self.myframe.play_sound('click'), self.myframe.change_frame("Main_Menu")))
        back.place(x=20, y=530)
