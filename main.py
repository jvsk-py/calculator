#ayyy this is the start of a 1000 mile journey with a single step (or comment lol😂😂😂)

#LAUGH RIGHT NOW

import tkinter as tk

#main calculation stuyff

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    result_text.delete(1.0, tk.END)
    result_text.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, result)
        calculation = result
    except Exception: #so that it doesn't say "Error" when I keyboard interrupt
        calculation = "Error"
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, calculation)
        root.after(500, lambda: result_text.delete(1.0, tk.END)) #34 MIN LONGEST DEBUG BECAUSE I TRIED MAKING IT MYSELF, ALL I HAD TO DO WAS ADD LAMBDA
        calculation = ""
        


    
def clear_calculation():
    global calculation
    calculation = ""
    result_text.delete(1.0, tk.END)

root = tk.Tk()
bg = "#000d24"

#lay the foundation or whatever

root.title("My First GUI")
#making the window look so pretty and so beautiful and just looking like a wow
root.title("W calc")
root.config(bg=bg) #midnigght blue so tuff
root.geometry("400x553") #size of the window
root.resizable(False, False) #cant resize the window haha imagine trying to resize this hahaha😂😂😂😂

#all the buttons


result_text = tk.Text(root, height=2, width=14, font=("Arial", 35), bg="#000d24", fg="white", bd=0, highlightthickness=0)
result_text.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_1.grid(row=1, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_2.grid(row=1, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_3.grid(row=1, column=2)

btn_clear = tk.Button(root, text="C", command=clear_calculation, width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_clear.grid(row=1, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_6.grid(row=2, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_plus.grid(row=2, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_7.grid(row=3, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_8.grid(row=3, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_9.grid(row=3, column=2)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_minus.grid(row=3, column=3)

btn_square = tk.Button(root, text="x²", command=lambda: add_to_calculation("**2"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_square.grid(row=4, column=0)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_0.grid(row=4, column=1)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_multiply.grid(row=4, column=2)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_divide.grid(row=4, column=3)

btn_period = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_period.grid(row=5, column=2)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_equals.grid(row=5, column=3)

btn_paranthesis_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_paranthesis_open.grid(row=5, column=0)

btn_paranthesis_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, height=2, font=("Arial", 20), bg="#000d24", fg="white", bd=0, highlightthickness=0, borderwidth=2)
btn_paranthesis_close.grid(row=5, column=1)



#oooooooooohhh, stayin' alive, stayin' alive
root.mainloop()