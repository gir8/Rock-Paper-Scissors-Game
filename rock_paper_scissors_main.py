"""A work in progress of a program for rock paper scissors."""
import random
import customtkinter as ctk
from tkinter import Menu, messagebox
import rps_lower as screen
import time


class RPS(ctk.CTk):
    def __init__(self):
        super().__init__()
        # setup
        self.title("Rock Paper Scissors")
        self.geometry("500x500")

        # menu
        menubar = Menu(self, background='#ff8000', foreground='black', activebackground='white',
                       activeforeground='black')
        file = Menu(menubar, tearoff=0)
        file.add_command(label='New Game', command=self.play_again)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="About", command=self.about)
        menubar.add_cascade(label='File', menu=file)
        menubar.add_cascade(label='About', menu=about)
        self.configure(menu=menubar)

        # data
        self.text_var = ctk.StringVar(value="")
        self.button_var = ""
        self.win = 0
        self.loss = 0
        self.tie = 0

        # gui
        self.draw_screen()
        self.create_bottom = screen.Create_Bottom(parent=self, player=self.player)

        # Start
        self.write_to_text()

    def about(self):
        messagebox.showinfo(title="about", message="Gir8 Muffin Games")

    def draw_screen(self):
        top_frame = ctk.CTkFrame(self, fg_color="#a958f7", corner_radius=0)
        top_frame.pack(expand=False, fill="both", anchor="n")
        self.screen = ctk.CTkLabel(master=top_frame,
                                   bg_color="transparent",
                                   corner_radius=15,
                                   textvariable=self.text_var,
                                   fg_color="#000000",
                                   font=("Times New Roman", 28, "bold"),
                                   text_color="#00FF77",
                                   justify="left",
                                   anchor="nw",
                                   width=470,
                                   height=300)
        self.screen.grid(column=0, row=0, sticky="w", padx=15, pady=(15, 1))

    def player(self, button_var):
        self.button_var = button_var.lower()

        # computer turn
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices).lower()

        # compares the button_var to the player_var
        if self.button_var == computer:
            self.write_to_text(button_var=button_var, computer=computer, text="Tie!")
            self.tie += 1
            self.update()
        elif (self.button_var == "rock" and computer == "scissors") or (self.button_var == "paper" and computer == "rock") or (self.button_var == "scissors" and computer == "paper"):
            self.write_to_text(button_var=button_var, computer=computer, text="You win!")
            self.win += 1
            self.win_or_lose()
        else:
            self.write_to_text(button_var=button_var, computer=computer, text="You lose!")
            self.loss += 1
            self.win_or_lose()

    def write_to_text(self, button_var=None, computer=None, text=""):
        if button_var:
            write = ["Computer: ", computer.title() + "\n", "Player: ", button_var.title() + "\n", text + "\n"]
            self.screen.configure(justify="left",
                                  anchor="nw",
                                  font=("Times New Roman", 28, "bold"),
                                  text_color="#00FF77")
        elif self.win == 3:
            write = ["You won!\n",  "Yokatta desu ne!\n"]
            self.screen.configure(justify="center",
                                  anchor="center",
                                  font=("Times New Roman", 44, "bold"),
                                  text_color="#00AAFF")
        elif self.loss == 3:
            write = ["You loss!\n",  "Sumimasen!\n"]
            self.screen.configure(justify="center",
                                  anchor="center",
                                  font=("Times New Roman", 44, "bold"),
                                  text_color="#FF4400")
        else:
            write = ["Rock,\n", "Paper,\n", "Scissors!"]
            self.screen.configure(justify="center",
                                  anchor="center",
                                  font=("Times New Roman", 28, "bold"),
                                  text_color="#00FF77")

        # clears the screen
        self.text_var.set("")

        self.change_state("disabled")
        for line in write:
            for c in line:
                original = self.text_var.get()
                self.text_var.set(original + c)
                time.sleep(0.07)
                self.update()
            time.sleep(0.20)
        self.change_state("enabled")

    def win_or_lose(self):
        if self.loss == 3:
            self.write_to_text()
            answer = messagebox.askyesno(title="Game Finished", message="Do you want to play again?")
            if answer:
                self.loss = 0
                self.win = 0
                self.write_to_text()
            else:
                quit()
        elif self.win == 3:
            self.write_to_text()
            answer = messagebox.askyesno(title="Game Finished", message="Do you want to play again?")
            if answer:
                self.loss = 0
                self.win = 0
                self.write_to_text()
            else:
                quit()
        else:
            pass

    def play_again(self):
        self.win = 0
        self.loss = 0
        self.write_to_text()

    def change_state(self, status: str):
        self.create_bottom.rock.configure(state=status)
        self.create_bottom.paper.configure(state=status)
        self.create_bottom.scissors.configure(state=status)


rps = RPS().mainloop()
