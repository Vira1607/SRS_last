import random
import math
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox

def snowflake():
    for x in range(0, 8):
        color = random.choice(colours)
        colours.remove(color)
        color_other = random.choice(colours)
        return color, color_other


def lightflake():
    for x in range(0, 1):
        color = random.choice(colours_light)
        return color


def result():
    a = name.get()
    b = name_2.get()
    alpha = name_3.get()
    # print(a, b, alpha)
    return float(a), float(b), float(alpha)

def result_1():
    a, b, alpha = result()
    c = b ** (alpha - 1) / (alpha - 1) - a ** (alpha - 1) / (alpha - 1)
    Label(text=f'Интеграл от x в степени {alpha} в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_2():
    a, b, alpha = result()
    c = math.log(b) - math.log(a)
    Label(text=f'Интеграл от 1 / x в степени в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_3():
    a, b, alpha = result()
    c = math.exp(a) - math.exp(b)
    Label(text=f'Интеграл от экспоненты в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_4():
    a, b, alpha = result()
    c = alpha ** (b) / math.log(alpha) - alpha ** (a) / math.log(alpha)
    answer = Label(text=f'Интеграл от {alpha} в степени x в пределах от {a} до {b} равен {c}', background=color_1)
    answer.grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_5():
    a, b, alpha = result()
    c = math.sin(b) - math.sin(a)
    Label(text=f'Интеграл от косинуса x в степени в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_6():
    a, b, alpha = result()
    c = math.cos(a) - math.cos(b)
    Label(text=f'Интеграл от синуса в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_7():
    a, b, alpha = result()
    c = math.tan(b) - math.tan(a)
    Label(text=f'Интеграл от 1 / (cos(x)^2) в пределах от {a} до {b} равен {c}', background=color_1).grid(row=7, column=0, columnspan=5, padx=15, pady=10)

def result_8():
    a, b, alpha = result()
    c = 1 / math.tan(a) - 1 / math.tan(b)
    answer = Label(text=f'Интеграл от 1 / (sin(x)^2) в пределах от {a} до {b} равен {c}', background=color_1)
    answer.grid(row=7, column=0, columnspan=5, padx=15, pady=10)

colours = ["#BFFEE6", "#009999", "#FFCCCC", "#CCCCFF", "#CC99FF", "#FFCCFF", '#FF9696', '#FFB5F5']

colours_light = ['#FFF076', '#FEDB51', '#F09F65', '#CCFF99', '#99FFCC', '#FFFFCC']

color_1, color_2 = snowflake()

color_3 = lightflake()

win = tk.Tk()
win.geometry(f'500x500+100+200')
win.configure(bg=color_1)
win.title('Вычисление интегралов')

tk.Label(win, text='Введите a: ',
         padx=15, pady=10, bg=color_1).grid(row=0, column=0)
name = tk.Entry(win)
name.grid(row=0, column=1)

tk.Label(win, text='Введите b: ',
         padx=15, pady=10, bg=color_1).grid(row=1, column=0)
name_2 = tk.Entry(win)
name_2.grid(row=1, column=1)

tk.Label(win, text='Введите альфа: ',
         padx=15, pady=10, bg=color_1).grid(row=0, column=3)
name_3 = tk.Entry(win)
name_3.grid(row=0, column=4)


text = tk.Label(win, text='Выберите основание интеграла ',
                padx=15, pady=10, bg=color_1)
text.grid(row=2, column=0, columnspan=4, padx=15, pady=10)

tk.Button(win, text='\u222B x^a dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_1).grid(row=3, column=0, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B 1/x dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_2).grid(row=4, column=0, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B e^x dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_3).grid(row=5, column=0, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B a^x dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_4).grid(row=6, column=0, columnspan=2, padx=15, pady=10)

tk.Button(win, text='\u222B cos(x) dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_5).grid(row=3, column=3, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B sin(x) dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_6).grid(row=4, column=3, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B 1 / (cos(x)^2) dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_7).grid(row=5, column=3, columnspan=2, padx=15, pady=10)
tk.Button(win, text='\u222B 1 / (sin(x)^2) dx', padx=15, pady=10, bg=color_2,
          activebackground=color_3, command=result_8).grid(row=6, column=3, columnspan=2, padx=15, pady=10)

win.mainloop()
