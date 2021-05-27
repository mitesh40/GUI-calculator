import tkinter as tk
from tkinter import ttk
exp = " "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)

def equalpress():

    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "

    except:

        equation.set('error')
        exp = " "


def clear():

    global exp
    exp = " "
    equation.set(" ")

if __name__ == "__main__" :

    root = tk.Tk()
    root.title('Calculator')
    root.iconbitmap('Calculator.ico')
    root.geometry('258x170')
    root.maxsize(width=258,height=170)

    root.configure(bg='blue')


equation = tk.StringVar()
dis_entry = ttk.Entry(root,width = 40, state = 'readonly',  background = 'red' , textvariable = equation)
dis_entry.grid(row = 0, columnspan = 10 , ipadx = 6, ipady = 8)
dis_entry.focus()

btn7 = ttk.Button(root, text='7' , width = 5, command = lambda : press(7))
btn7.grid(row = 1 , column = 0, ipady = 4, ipadx = 2)

btn8 = ttk.Button(root, text='8' , width = 5, command = lambda : press(8))
btn8.grid(row = 1 , column = 1, ipady = 4, ipadx = 2)

btn9 = ttk.Button(root, text='9' , width = 5, command = lambda : press(9))
btn9.grid(row = 1 , column = 2, ipady = 4, ipadx = 2)

btn6 = ttk.Button(root, text='6' , width = 5, command = lambda : press(6))
btn6.grid(row = 2 , column = 2, ipady = 4, ipadx = 2)

btn5 = ttk.Button(root, text='5' , width = 5, command = lambda : press(5))
btn5.grid(row = 2 , column = 1, ipady = 4, ipadx = 2)

btn4 = ttk.Button(root, text='4' , width = 5, command = lambda : press(4))
btn4.grid(row = 2 , column = 0, ipady = 4, ipadx = 2)

btn3 = ttk.Button(root, text='3' , width = 5, command = lambda : press(3))
btn3.grid(row = 3 , column = 2, ipady = 4, ipadx = 2)

btn2 = ttk.Button(root, text='2' , width = 5, command = lambda : press(2))
btn2.grid(row = 3 , column = 1, ipady = 4, ipadx = 2)

btn1 = ttk.Button(root, text='1' , width = 5, command = lambda : press(1))
btn1.grid(row = 3 , column = 0, ipady = 4, ipadx = 2)

btnmines = ttk.Button(root, text = '-', width = 8, command = lambda : press('-'))
btnmines.grid(row = 1, column = 3, ipady = 3, ipadx = 2)

btnmul = ttk.Button(root, text = '*', width = 8, command = lambda : press('*'))
btnmul.grid(row = 1, column = 4, ipady = 3, ipadx = 2)

btnadd = ttk.Button(root, text = '+', width = 8, command = lambda : press('+'))
btnadd.grid(row = 2, column = 3, ipady = 3, ipadx = 2)

btndivide = ttk.Button(root, text = '/', width = 8, command = lambda : press('/'))
btndivide.grid(row = 2, column = 4, ipady = 3, ipadx = 2)

btnequal = ttk.Button(root, text = '=', width = 8, command = lambda : press('='))
btnequal.grid(row = 3, column = 4, ipady = 3, ipadx = 2)

root.mainloop()
            
                    
