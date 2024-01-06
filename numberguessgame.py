import tkinter as tk
from tkinter import *
import random

def check_guess():
    x = guess.get()
    final_score.set(Score.get())
    if Score.get() > 0:
        if x > 50 or x < 1:
            hint.set("You just lost 1 chance")
            Score.set(Score.get() - 1)
            final_score.set(Score.get())
        elif num == x:
            hint.set("Congratulations YOU WON!!!")
            Score.set(Score.get() - 1)
            final_score.set(Score.get())
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            Score.set(Score.get() - 1)
            final_score.set(Score.get())
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            Score.set(Score.get() - 1)
            final_score.set(Score.get())
    else:
        hint.set("Game Over You Lost")
        check_button.config(state=tk.DISABLED)  # Disable the button when the game is over
        
win = tk.Tk()
win.geometry("750x750")
win.title("pythonGeeks")

guess = tk.IntVar()
hint = tk.StringVar()
Score = tk.IntVar()
final_score = tk.IntVar()

Entry(win, textvariable=guess, width=3, font=('ubuntu', 50), relief=tk.GROOVE).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
Entry(win, textvariable=hint, width=50, font=('courier', 15), relief=tk.GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=tk.CENTER)
Entry(win, text=final_score, width=2, font=('courier', 15), relief=tk.GROOVE, bg='orange').place(relx=0.61, rely=0.85, anchor=tk.CENTER)

tk.Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=tk.CENTER)
tk.Label(win, text='Score out of 5', font=('Courier', 25)).place(relx=0.3, rely=0.85, anchor=tk.CENTER)

check_button = tk.Button(win, width=8, text='CHECK', font=('Courier', 25), command=check_guess, relief=tk.GROOVE, bg='light blue')
check_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

num = random.randint(1, 50)
hint.set("Guess a number between 1 to 50")
Score.set(5)
final_score.set(Score.get())

win.mainloop()
