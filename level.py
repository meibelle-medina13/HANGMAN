import tkinter as tk

class Level(tk.Frame):
    def __init__(self, parent, myframe):
        tk.Frame.__init__(self, parent)
        self.myframe = myframe

        self.d_buttons = {"Country":{"current level": 0}, "Food":{"current level": 0}, "Sports":{"current level": 0}, "Social Media":{"current level": 0}}
        self.topframe = tk.Frame(self, bg="white", height=600, width=900)
        self.topframe.place(x=0, y=0)

    def title_bg(self):

        self.myframe.background_image(self.topframe)
        self.title = tk.Label(self.topframe, text="Levels", font=("Comic Sans Ms", 50), bg="white")
        self.title.place(x=340, y=30)

    def for_scrollbar(self):
        self.canvas = tk.Canvas(self.topframe, width=300, height=300)
        
        self.level_frame = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(self.topframe, orient="vertical", command=self.canvas.yview)

        self.level_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0,0), window=self.level_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll.set)

    def buttons(self, index_cat):

        for child in self.topframe.winfo_children():
            child.destroy()

        self.string_category = ["Country", "Food", "Sports", "Social Media"]
        self.current_cat = self.string_category[index_cat]
        self.current_lev = self.get_current_level()

        self.title_bg()
        self.for_scrollbar()

        self.levels = []

        with open(f"./levels/{self.current_cat}.txt") as f:
            self.levels = f.read().split("\n")

        for level in range(0, len(self.levels)):
            
            def get_button_val(val = level):
                return (self.myframe.play_sound("click"), self.pass_level(val))
            
            self.d_buttons[self.current_cat][(level+1)] = tk.Button(self.level_frame, text="Level " + str(level+1), bg="light gray", font=("Comic Sans Ms", 25), width=15, command=get_button_val, state=tk.DISABLED if self.current_lev < level else tk.NORMAL)
            self.d_buttons[self.current_cat][(level+1)].pack(padx=0)

        self.canvas.pack(padx=290, pady=200, side="left")
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        back = tk.Button(self.topframe, text="Back", bg="light gray", font=("Comic Sans Ms", 15), width=10, command=lambda:(self.myframe.play_sound("click"), self.myframe.change_frame("Category")))
        back.place(x=20, y=530)

    def set_current_level(self, level):
        self.d_buttons[self.current_cat]["current level"] = level
        return level
    
    def get_current_level(self):
        return self.d_buttons[self.current_cat]["current level"]

    def get_levels(self):
        return self.levels
    
    def pass_level(self, level):
        self.current_lev = level + 1
        self.myframe.subframes["Game_Space"].get_level(self.current_lev, self.current_cat)
        self.myframe.subframes["Game_Space"].answer_screen(self.levels[level])
        self.myframe.change_frame("Game_Space")
