#ayyy this is the start of a 1000 mile journey with a single step (or comment lol😂😂😂)

#LAUGH RIGHT NOW

import tkinter as tk

#main calculation stuyff

calculation = ""

def add_to_calculation(symbol):
    pass

def evaluate_calculation():
    pass

def clear_calculation():
    pass






root = tk.Tk()
bg = "#000d24"

#lay the foundation or whatever

root.title("My First GUI")
#making the window look so pretty and so beautiful and just looking like a wow
root.title("W calc")
root.config(bg=bg) #midnigght blue so tuff
root.geometry("400x650") #size of the window
root.resizable(False, False) #cant resize the window haha imagine trying to resize this hahaha😂😂😂😂


label = tk.Label(root, text="yo wassup", bg=bg, fg="white")
label.pack()
button = tk.Button(root, text="click me or else ull see", command=lambda: label.config(text="ur such a good boy"), bg=bg, fg="white")
button.pack()

#oooooooooohhh, stayin' alive, stayin' alive
root.mainloop()