import tkinter as tk

window = tk.Tk()
window.geometry("300x350")
window.title("Calculator App")

equation_text = ""
def button_press(sym):
    global equation_text
    equation_text += str(sym)
    label.config(text=equation_text)

def evaluate():
    global equation_text
    try:
        total = str(eval(equation_text))
        label.config(text=total)
        equation_text = ""
    except:
        label.config(text="Error")
        equation_text = ""

def reset():
    global equation_text
    equation_text = ""
    label.config(text=equation_text)


label = tk.Label(window, text="", width=8, height=2, font= ("arial", 14))
label.grid()

btn_1 = tk.Button(window, text= "1",  width=3, height=2, command= lambda : button_press("1"), font= ("arial", 10))
btn_1.grid(row=1,column=0, padx=5, pady=8)

btn_2 = tk.Button(window, text= "2", width=3, height=2, command= lambda : button_press("2"), font= ("arial", 10))
btn_2.grid(row=1,column=1, padx=5, pady=8)

btn_3 = tk.Button(window, text= "3", width=3, height=2, command= lambda : button_press("3"), font= ("arial", 10))
btn_3.grid(row=1,column=2, padx=5, pady=8)

plus = tk.Button(window, text= "+", width=3, height=2, command= lambda : button_press("+"), font= ("arial", 10))
plus.grid(row=1,column=3, padx=5, pady=8)

btn_4 = tk.Button(window, text= "4", width=3, height=2, command= lambda : button_press("4"), font= ("arial", 10))
btn_4.grid(row=2,column=0, padx=5, pady=8)

btn_5 = tk.Button(window, text= "5", width=3, height=2, command= lambda : button_press("5"), font= ("arial", 10))
btn_5.grid(row=2,column=1, padx=5, pady=8)

btn_6 = tk.Button(window, text= "6", width=3, height=2, command= lambda : button_press("6"), font= ("arial", 10))
btn_6.grid(row=2,column=2, padx=5, pady=8)

minus = tk.Button(window, text= "-", width=3, height=2, command= lambda : button_press("-"), font= ("arial", 10))
minus.grid(row=2,column=3, padx=5, pady=8)

btn_7 = tk.Button(window, text= "7", width=3, height=2, command= lambda : button_press("7"), font= ("arial", 10))
btn_7.grid(row=3,column=0, padx=5, pady=8)

btn_8 = tk.Button(window, text= "8", width=3, height=2, command= lambda : button_press("8"), font= ("arial", 10))
btn_8.grid(row=3,column=1, padx=5, pady=8)

btn_9 = tk.Button(window, text= "9", width=3, height=2, command= lambda : button_press("9"), font= ("arial", 10))
btn_9.grid(row=3,column=2, padx=5, pady=8)

multiply = tk.Button(window, text= "*", width=3, height=2, command= lambda : button_press("*"), font= ("arial", 10))
multiply.grid(row=3,column=3, padx=5, pady=8)

btn_0 = tk.Button(window, text= "0", width=3, height=2, command= lambda : button_press("0"), font= ("arial", 10))
btn_0.grid(row=4,column=0, padx=5, pady=8)

decimal = tk.Button(window, text= ".", width=3, height=2, command= lambda : button_press("."), font= ("arial", 10))
decimal.grid(row=4,column=1, padx=5, pady=8)

equal = tk.Button(window, text= "=", width=3, height=2, command= evaluate, font= ("arial", 10))
equal.grid(row=4,column=2, padx=5, pady=8)

divide = tk.Button(window, text= "/", width=3, height=2, command= lambda : button_press("/"), font= ("arial", 10))
divide.grid(row=4,column=3, padx=5, pady=8)

clear = tk.Button(window, text= "clear", width=3, height=2, command= reset)
clear.grid(row=5, padx=5, pady=8)

window.mainloop()


