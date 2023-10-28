from tkinter import Menu
import customtkinter as ctk
# import rock_paper_scissors_main as rpsm


class Create_Bottom(ctk.CTkFrame):
    def __init__(self, parent: object, player: classmethod):
        super().__init__(parent, fg_color="#a958f7", corner_radius=0)
        self.pack(expand=True, fill="both", anchor="n")
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        rock = ctk.CTkButton(master=self,
                             width=100,
                             height=100,
                             fg_color="#FF0085",
                             text="Rock",
                             state="normal",
                             border_width=5,
                             border_color="#FF0055",
                             hover_color="#FF0025",
                             font=("Times New Roman", 22, "bold"),
                             command=lambda: player(button_var="rock"))
        rock.grid(column=0, row=0)
        paper = ctk.CTkButton(master=self,
                              width=100,
                              height=100,
                              fg_color="#FF0085",
                              text="Paper",
                              state="normal",
                              border_width=5,
                              border_color="#FF0055",
                              hover_color="#FF0025",
                              font=("Times New Roman", 22, "bold"),
                              command=lambda: player(button_var="paper"))
        paper.grid(column=1, row=0)
        scissors = ctk.CTkButton(master=self,
                                 width=100,
                                 height=100,
                                 fg_color="#FF0080",
                                 text="Scissors",
                                 state="normal",
                                 border_width=5,
                                 border_color="#FF0055",
                                 hover_color="#FF0025",
                                 font=("Times New Roman", 22, "bold"),
                                 command=lambda: player(button_var="scissors"))
        scissors.grid(column=2, row=0)

    def game(self):
        RPS()

    def run(self):
        self.mainloop()


# run = RPS_User()
# run.run()
