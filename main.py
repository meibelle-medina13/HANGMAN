import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
from main_menu import Main_Menu
from category import Category
from level import Level
from game_space import Game_Space
from mechanics import Mechanics

class Hangman(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        mixer.init()

        mainframe = tk.Frame(self)
        mainframe.pack(side="top", fill="both", expand=True)

        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        self.subframes = {}
        for frame in (Main_Menu, Level, Category, Game_Space, Mechanics):
            current_frame = frame(mainframe, self)
            self.subframes[frame.__name__] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")
            
        self.background_sound()
        self.change_frame("Main_Menu")

    def background_sound(self):
        mixer.music.load('./resources/sounds/background.mp3')
        mixer.music.set_volume(1)
        mixer.music.play(-1)

    def change_frame(self, frame):
        show = self.subframes[frame]
        show.tkraise()

    def background_image(self, frame):
        bg_image = Image.open("./resources/images/main.png")
        resize = bg_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resize)

        bg_image_label = tk.Label(frame, background="white", image=img)
        bg_image_label.image = img
        bg_image_label.place(x=13, y=80)
    
    def play_sound(self, sound):
        mixer.Channel(0).play(mixer.Sound(f"./resources/sounds/{sound}.mp3"))

    def run(self):
        self.title("HangMan Game")
        self.geometry("900x600")
        self.resizable(False, False)
        self.mainloop()

app = Hangman()
app.run()
