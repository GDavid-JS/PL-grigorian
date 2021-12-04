from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Пошвин Иван Сергеевич")
window.geometry('450x500')
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [5, 5, 5, 5]}},
        "TNotebook.Tab": {"configure": {"padding": [30, 30, 30, 30]}, }})
style.theme_use("MyStyle")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая вкладка')
tab_control.add(tab2, text='Вторая вкладка')
tab_control.add(tab3, text='Третья вкладка')
lbl1 = Label(tab1, text='Вкладка 1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)
lbl3 = Label(tab3, text='Вкладка 3')
lbl3.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
from tkinter import messagebox
import math
def add_digit(digit):
    value=calc.get()
    if value[0]=="0" and len(value)==1:
        value=value[1:]
    calc.delete(0,END)
    calc.insert(0,value+digit)
def add_operation(operation):
    value=calc.get()
    if value[-1] in "-+/*":
        value=value[:-1]
    elif "+" in value or "-" in value or"*" in value or"/" in value:
        calculate()
        value=calc.get()
    calc.delete(0,END)
    calc.insert(0,value+operation)
def calculate():
    value=calc.get()
    if value[-1] in "-+/*":
        value=value+value[:-1]
    calc.delete(0,END)
    try:
        calc.insert(0,eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Внимание!","Нужно вводить только цифры и числа!")
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo("Внимание!","На ноль делить нельзя!")
        calc.insert(0,0)
def add_sqrt():
    value=calc.get()
    value=float(value)
    value=math.sqrt(value)
    calc.delete(0,END)
    calc.insert(0,value)
def add_fabs():
    value=calc.get()
    value=eval(value)
    value=math.fabs(value)
    calc.delete(0,END)
    calc.insert(0,value)     
def clear():
    calc.delete(0,END)
    calc.insert(0,0)
def make_calc_button(operation):
    return Button(tab1,text=operation,bd=5,font=("Nyala",14),
                     command=calculate)
def make_clear_button(operation):
    return Button(tab1,text=operation,bd=5,font=("Nyala",14),
                     command=clear)
def make_operation_button(operation):
    return Button(tab1,text=operation,bd=5,font=("Nyala",14),
                     command=lambda:add_operation(operation))
def make_sqrt_button(operation):
    return Button(tab1,text=operation,image=img,bd=5,font=("Nyala", 14),
                     command=add_sqrt)
def make_fabs_button(operation):
    return Button(tab1,text=operation,bd=5,font=("Nyala",14),
                     command=add_fabs)
def make_digit_button(digit):
    return Button(tab1,text=digit,bd=5,font=("Nyala",14),
                     command=lambda:add_digit(digit))
# tk=Tk()
# tk.geometry("265x365+105+205")
# tk.title("Пошвин Иван Сергеевич")
# tk.resizable(0,0)
# tk["bg"]="turquoise"
calc=Entry(tab1,justify=RIGHT,font=("Nyala",16), width=16)
calc.insert(0,"0")
calc.place(x=20,y=25,width=230,height=35)
make_digit_button("1").place(x=20,y=250,width=40,height=40)
make_digit_button("2").place(x=80,y=250,width=40,height=40)
make_digit_button("3").place(x=140,y=250,width=40,height=40)
make_digit_button("4").place(x=20,y=190,width=40,height=40)
make_digit_button("5").place(x=80,y=190,width=40,height=40)
make_digit_button("6").place(x=140,y=190,width=40,height=40)
make_digit_button("7").place(x=20,y=130,width=40,height=40)
make_digit_button("8").place(x=80,y=130,width=40,height=40)
make_digit_button("9").place(x=140,y=130,width=40,height=40)
make_digit_button("0").place(x=20,y=310,width=100,height=40)
make_digit_button(".").place(x=140,y=310,width=40,height=40)
make_operation_button("+").place(x=200,y=310,width=40,height=40)
make_operation_button("-").place(x=200,y=250,width=40,height=40)
make_operation_button("*").place(x=200,y=190,width=40,height=40)
make_operation_button("/").place(x=200,y=130,width=40,height=40)
make_clear_button("C").place(x=20,y=70,width=40,height=40)
make_calc_button("=").place(x=200,y=70,width=40,height=40)
window.mainloop()

