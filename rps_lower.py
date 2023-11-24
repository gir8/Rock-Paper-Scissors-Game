from tkinter import Menu
import customtkinter as ctk


class Create_Bottom(ctk.CTkFrame):
    def __init__(self, parent: object, player: classmethod):
        super().__init__(parent, fg_color="#a958f7", corner_radius=0)
        self.pack(expand=True, fill="both", anchor="n")
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        self.rock = ctk.CTkButton(master=self,
                                  width=100,
                                  height=100,
                                  fg_color="#FF0085",
                                  text_color_disabled="#777777",
                                  text="Rock",
                                  state="normal",
                                  border_width=5,
                                  border_color="#FF0055",
                                  hover_color="#FF0025",
                                  font=("Times New Roman", 22, "bold"),
                                  command=lambda: player(button_var="rock"))
        self.rock.grid(column=0, row=0)
        self.paper = ctk.CTkButton(master=self,
                                   width=100,
                                   height=100,
                                   fg_color="#FF0085",
                                   text_color_disabled="#777777",
                                   text="Paper",
                                   state="normal",
                                   border_width=5,
                                   border_color="#FF0055",
                                   hover_color="#FF0025",
                                   font=("Times New Roman", 22, "bold"),
                                   command=lambda: player(button_var="paper"))
        self.paper.grid(column=1, row=0)
        self.scissors = ctk.CTkButton(master=self,
                                      width=100,
                                      height=100,
                                      fg_color="#FF0080",
                                      text="Scissors",
                                      text_color_disabled="#777777",
                                      state="normal",
                                      border_width=5,
                                      border_color="#FF0055",
                                      hover_color="#FF0025",
                                      font=("Times New Roman", 22, "bold"),
                                      command=lambda: player(button_var="scissors"))
        self.scissors.grid(column=2, row=0)

