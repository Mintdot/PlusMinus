import threading
from tkinter import *

def Plus():
    global num

    if num >= 400:
        num = 0
        number.configure(text=num)
        explain.configure(text="초기값으로 돌아갑니다")

    else:
        num += 100
        number.configure(text=num)
        explain.configure(text="매우 정상적이다")

def Minus():
    global num

    if num <= 0:
        num = 0
        number.configure(text=num)
        explain.configure(text="더 이상 감소되지 않습니다")
    else:
        num -= 100
        number.configure(text=num)
        explain.configure(text="매우 정상적이다")

def Go():
    global num

    if num >= 400:
        num = 0
        number.configure(text=num)
        explain.configure(text="초기값으로 돌아갑니다")

    else:
        num += 100
        number.configure(text=num)
        explain.configure(text="매우 정상적이다")

    timer = threading.Timer(1, Go)
    timer.start()

num = 0


root = Tk()
root.geometry("250x100+450+100")
frame1 = Frame(root)
frame2 = Frame(root)
explain = Label(frame1, text="매우 정상적이다", font=("", 13))
number = Label(frame1, text=num, font=("", 13))
M_Button = Button(frame2, text=" - ", command=Minus, width=5, height=2)
P_Button = Button(frame2, text=" + ", command=Plus, width=5, height=2)

frame1.pack(pady=5)
frame2.pack(pady=5)
explain.pack()
number.pack()
M_Button.pack(side=LEFT, padx=15)
P_Button.pack(side=RIGHT, padx=15)

Go()

root.mainloop()