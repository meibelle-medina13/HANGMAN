import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

class Game_Space(tk.Frame):

    def __init__(self, parent, myframe):
        tk.Frame.__init__(self, parent)
        self.myframe = myframe

        self.answer = []
        self.count = 0

        self.topframe = tk.Frame(self, bg="white", height=600, width=900)
        self.topframe.place(x=0, y=0)

        self.image_label = tk.Label(self.topframe, bg="white")
        self.image_label.place(x=450, y=20)

        self.keyboard_frame = tk.Frame(self.topframe, bg="white", height=270, width=900)
        self.keyboard_frame.place(x=0, y=340)

        self.cat_label = tk.Label(self.topframe, font=("Comic Sans Ms", 20, "bold"), bg="white")
        self.cat_label.place(x=20, y=20)
        self.level_label = tk.Label(self.topframe, font=("Comic Sans Ms", 30, "bold"), bg="white")
        self.level_label.place(x=20, y=60)
        self.ans_label = tk.Label(self.topframe, font=("Comic Sans Ms", 20, "bold"), bg="white", width=30)
        self.ans_label.place(x=10, y=250)

        self.image("./resources/images/0.png")
        self.buttons()
    
    def image(self, name):
        image = Image.open(name)
        resize = image.resize((850, 400))
        img = ImageTk.PhotoImage(resize)

        self.image_label.config(image=img)
        self.image_label.image = img

    def get_level(self, level, category):
        self.level = level
        self.category = category
        self.cat_label.config(text="Category: " + category)
        self.level_label.config(text="Level " + str(level))

    def set_word_level(self, level):
        self.word = self.myframe.subframes["Level"].get_levels()[level-1]

    def get_word_level(self):
        return self.word

    def answer_screen(self, word):
        self.list_word = [i for i in word]

        for letter in self.list_word:
            if letter == " ":
                self.answer.append("-")
            else:
                self.answer.append("_")
        
        self.ans_label.config(text=self.answer)

    def clicked_letter(self, letter, button):
        if letter not in self.list_word:
            self.myframe.play_sound('incorrect')
            button.config(state=tk.DISABLED, bg="pink")
            self.count += 1
            self.image(f"./resources/images/{str(self.count)}.png")
            if self.count == 8:
                self.count = 0
                self.outcome = "lose"
                thread = threading.Thread(target=self.result)
                thread.start()
        else:
            self.myframe.play_sound('correct')
            button.config(bg="light green", state=tk.DISABLED)
            for index, element in enumerate(self.list_word):
                if element == letter:
                    self.answer[index] = element

        self.ans_label.config(text=self.answer)

        if "_" not in self.answer:
            self.outcome = "win"
            thread = threading.Thread(target=self.result)
            thread.start()
        
    def refresh(self):
        for child in self.keyboard_frame.winfo_children():
            child.config(state=tk.NORMAL, bg="light gray", fg="black")
        self.count = 0
        self.wrong_button = []
        self.answer = []
        self.image(f"./resources/images/{str(self.count)}.png")
    
    def exit_gamespace(self):
        self.refresh()
        self.myframe.change_frame("Main_Menu")
    
    def buttons(self):
        self.buttonQ = tk.Button(self.keyboard_frame, text="Q", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("Q", self.buttonQ))
        self.buttonQ.place(x=70, y=0)
        self.buttonW = tk.Button(self.keyboard_frame, text="W", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("W", self.buttonW))
        self.buttonW.place(x=150, y=0)
        self.buttonE = tk.Button(self.keyboard_frame, text="E", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("E", self.buttonE))
        self.buttonE.place(x=230, y=0)
        self.buttonR = tk.Button(self.keyboard_frame, text="R", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("R", self.buttonR))
        self.buttonR.place(x=310, y=0)
        self.buttonT = tk.Button(self.keyboard_frame, text="T", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("T", self.buttonT))
        self.buttonT.place(x=390, y=0)
        self.buttonY = tk.Button(self.keyboard_frame, text="Y", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("Y", self.buttonY))
        self.buttonY.place(x=470, y=0)
        self.buttonU = tk.Button(self.keyboard_frame, text="U", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("U", self.buttonU))
        self.buttonU.place(x=550, y=0)
        self.buttonI = tk.Button(self.keyboard_frame, text="I", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("I", self.buttonI))
        self.buttonI.place(x=630, y=0)
        self.buttonO = tk.Button(self.keyboard_frame, text="O", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("O", self.buttonO))
        self.buttonO.place(x=710, y=0)
        self.buttonP = tk.Button(self.keyboard_frame, text="P", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("P", self.buttonP))
        self.buttonP.place(x=790, y=0)

        self.buttonA = tk.Button(self.keyboard_frame, text="A", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("A", self.buttonA))
        self.buttonA.place(x=110, y=85)
        self.buttonS = tk.Button(self.keyboard_frame, text="S", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("S", self.buttonS))
        self.buttonS.place(x=190, y=85)
        self.buttonD = tk.Button(self.keyboard_frame, text="D", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("D", self.buttonD))
        self.buttonD.place(x=270, y=85)
        self.buttonF = tk.Button(self.keyboard_frame, text="F", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("F", self.buttonF))
        self.buttonF.place(x=350, y=85)
        self.buttonG = tk.Button(self.keyboard_frame, text="G", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("G", self.buttonG))
        self.buttonG.place(x=430, y=85)
        self.buttonH = tk.Button(self.keyboard_frame, text="H", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("H", self.buttonH))
        self.buttonH.place(x=510, y=85)
        self.buttonJ = tk.Button(self.keyboard_frame, text="J", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("J", self.buttonJ))
        self.buttonJ.place(x=590, y=85)
        self.buttonK = tk.Button(self.keyboard_frame, text="K", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("K", self.buttonK))
        self.buttonK.place(x=670, y=85)
        self.buttonL = tk.Button(self.keyboard_frame, text="L", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("L", self.buttonL))
        self.buttonL.place(x=750, y=85)

        self.buttonZ = tk.Button(self.keyboard_frame, text="Z", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("Z", self.buttonZ))
        self.buttonZ.place(x=150, y=170)
        self.buttonX = tk.Button(self.keyboard_frame, text="X", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("X", self.buttonX))
        self.buttonX.place(x=230, y=170)
        self.buttonC = tk.Button(self.keyboard_frame, text="C", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("C", self.buttonC))
        self.buttonC.place(x=310, y=170)
        self.buttonV = tk.Button(self.keyboard_frame, text="V", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("V", self.buttonV))
        self.buttonV.place(x=390, y=170)
        self.buttonB = tk.Button(self.keyboard_frame, text="B", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("B", self.buttonB))
        self.buttonB.place(x=470, y=170)
        self.buttonN = tk.Button(self.keyboard_frame, text="N", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("N", self.buttonN))
        self.buttonN.place(x=550, y=170)
        self.buttonM = tk.Button(self.keyboard_frame, text="M", width=3, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:self.clicked_letter("M", self.buttonM))
        self.buttonM.place(x=630, y=170)

        exit = tk.Button(self.keyboard_frame, text="EXIT", width=5, bg="light gray", font=("Comic Sans Ms", 24), command=lambda:(self.myframe.play_sound('click'), self.exit_gamespace()))
        exit.place(x=710, y=170)

    def result(self):
        time.sleep(0.5)
        if self.outcome == "win":
            text = "YOU WIN!"
            self.myframe.play_sound('win')
            self.state2 = tk.NORMAL
            self.next_done = "Next"
        elif self.outcome == "lose":
            text = "YOU LOSE!"
            self.myframe.play_sound('lose')
            self.next_done = "Next"
            self.state2 = tk.DISABLED
        
        self.result_frame = tk.Frame(self.topframe, bg="white", height=470, width=500)
        self.result_frame.place(x=225, y=55)

        for child in self.topframe.winfo_children():
            if child == self.result_frame:
                continue
            else:
                child.config(bg="light gray")
        self.topframe.config(bg="light gray")

        for child in self.keyboard_frame.winfo_children():
            child.configure(state = tk.DISABLED)

        result_text = tk.Label(self.result_frame, text=text, bg="white", font=("Comic Sans Ms", 50))
        result_text.place(x=85, y=40)

        image = Image.open(f"./resources/images/{self.outcome}.png")
        resize = image.resize((600, 300))
        img = ImageTk.PhotoImage(resize)

        result_img = tk.Label(self.result_frame, bg="white", image=img)
        result_img.image = img
        result_img.place(x=0, y=130)

        if self.level == 1:
            self.state1 = tk.DISABLED
            self.choice_button()
        else:
            self.state1 = tk.NORMAL
            self.choice_button()
            if ((self.level) == 10 and self.outcome == "win") or ((self.level) == 10 and self.outcome == "lose"):
                self.next_done ="Done"
                self.choice_button()
                time.sleep(1)
    
    def choice_button(self):

        prev = tk.Button(self.result_frame, text="Prev", bg="light gray", font=("Comic Sans Ms", 20), width=6, state=self.state1, command=lambda:self.clicked_choice("Prev"))
        prev.place(x=10, y=380)
        replay = tk.Button(self.result_frame, text="Replay", bg="light gray", font=("Comic Sans Ms", 20), width=6, command=lambda:self.clicked_choice("Replay"))
        replay.place(x=200, y=380)
        nExt = tk.Button(self.result_frame, text=self.next_done, bg="light gray", font=("Comic Sans Ms", 20), width=6, state=self.state2, command=lambda:self.clicked_choice(self.next_done))
        nExt.place(x=380, y=380)

    def clicked_choice(self, choice):
        self.result_frame.destroy()
        self.image("./resources/images/0.png")

        for child in self.keyboard_frame.winfo_children():
            child.configure(state=tk.NORMAL)
        for child in self.topframe.winfo_children():
            child.config(bg="white")
        self.topframe.config(bg="white")

        thread = threading.Thread(target=self.refresh())  
        if choice == "Prev":
            self.myframe.play_sound('click')
            self.level -= 1
            self.level_label.config(text="Level " + str(self.level))
            thread.start()
            self.set_word_level(self.level)
            self.myframe.subframes["Game_Space"].answer_screen(self.get_word_level())
        
        elif choice == "Replay":
            self.myframe.play_sound('click')
            thread.start()
            self.set_word_level(self.level)
            self.myframe.subframes["Game_Space"].answer_screen(self.get_word_level())
        
        elif choice == "Next":
            self.myframe.play_sound('click')
            self.level += 1
            self.myframe.subframes["Level"].set_current_level(self.level-1)
            self.level_label.config(text="Level " + str(self.level))
            thread.start()
            self.set_word_level(self.level)
            self.myframe.subframes["Game_Space"].answer_screen(self.get_word_level())
        
        elif choice == "Done":
            self.myframe.play_sound('click')
            thread.start()
            self.myframe.change_frame("Category")
