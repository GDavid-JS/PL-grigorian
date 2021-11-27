from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
import math
import os.path
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
    return Button(tab_1, text=operation,bd=5,font=("Roboto",14),command=calculate, bg="#FFF")
def make_clear_button(operation):
    return Button(tab_1, text=operation,bd=5,font=("Roboto",14),command=clear, bg="#FFF")
def make_operation_button(operation):
    return Button(tab_1, text=operation,bd=5,font=("Roboto",14),command=lambda:add_operation(operation), bg="#FFF")
def make_sqrt_button(operation):
    return Button(tab_1, text=operation,bd=5,font=("Roboto", 14),command=add_sqrt, bg="#FFF")
def make_fabs_button(operation):
    return Button(tab_1, text=operation,bd=5,font=("Roboto",14), command=add_fabs, bg="#FFF")
def make_digit_button(digit):
    return Button(tab_1, text=digit,bd=5,font=("Roboto",14),command=lambda:add_digit(digit), bg="#FFF")

root = Tk()
root.title("Григорян Давид Жирайрович")
root.geometry("500x500")
root.resizable(False, False)

test = ttk.Notebook(root)
test.pack()

style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [5, 5, 5, 5]}},
        "TNotebook.Tab": {"configure": {"padding": [5, 5, 5, 5]}, }})

style.theme_use("MyStyle")

tab_1 = Frame(test, width=500, height=500)
tab_1["bg"] = "#000"
tab_1.pack()

tab_2 = Frame(test, width=500, height=500)
tab_2.pack()

tab_3 = Frame(test, width=500, height=500)
tab_3.pack()

test.add(tab_1, text="Калькулятор")
test.add(tab_2, text="Чекбокс")
test.add(tab_3, text="Загрузка текста из файла")


calc=Entry(tab_1,justify=RIGHT,font=("Roboto",16), width=16)
calc.insert(0,"0")
calc.place(x=20,y=20,width=238,height=40)

make_digit_button("1").place(x=20,y=250,width=60,height=60)
make_digit_button("2").place(x=80,y=250,width=60,height=60)
make_digit_button("3").place(x=140,y=250,width=60,height=60)
make_digit_button("4").place(x=20,y=190,width=60,height=60)
make_digit_button("5").place(x=80,y=190,width=60,height=60)
make_digit_button("6").place(x=140,y=190,width=60,height=60)
make_digit_button("7").place(x=20,y=130,width=60,height=60)
make_digit_button("8").place(x=80,y=130,width=60,height=60)
make_digit_button("9").place(x=140,y=130,width=60,height=60)
make_digit_button("0").place(x=20,y=310,width=120,height=60)
make_digit_button(".").place(x=140,y=310,width=60,height=60)
make_operation_button("+").place(x=200,y=310,width=60,height=60)
make_operation_button("-").place(x=200,y=250,width=60,height=60)
make_operation_button("*").place(x=200,y=190,width=60,height=60)
make_operation_button("/").place(x=200,y=130,width=60,height=60)
make_clear_button("C").place(x=20,y=70,width=60,height=60)
make_calc_button("=").place(x=200,y=70,width=60,height=60)

checkbutton_1_value = StringVar()
checkbutton_2_value = StringVar()
checkbutton_3_value = StringVar()

checkbutton_1 = Checkbutton(tab_2, text="Первый чекбокс", variable=checkbutton_1_value,offvalue="",onvalue="первый")
checkbutton_1.place(x=200,y=20)

checkbutton_2 = Checkbutton(tab_2, text="Второй чекбокс", variable=checkbutton_2_value,offvalue="",onvalue="второй")
checkbutton_2.place(x=200,y=40)

checkbutton_3 = Checkbutton(tab_2, text="Третий чекбокс", variable=checkbutton_3_value,offvalue="",onvalue="третий")
checkbutton_3.place(x=200,y=60)




def print_checkbutton_value():
        for checkbutton in [checkbutton_1_value, checkbutton_2_value, checkbutton_3_value]:
                if bool(checkbutton.get()):
                        messagebox.showinfo("Внимание!",f"Вы выбрали {checkbutton.get()}")

button = Button(tab_2, text="кнопка",bd=5,font=("Roboto", 14),command=print_checkbutton_value)
button.place(x=200, y=100)

text_1 = Label(tab_3)
text_1.place(x=28, y=70)

def import_text():
        input_text = input_path.get()
        if (os.path.isfile(input_text)):
                file = open(input_path.get())
                text_1.config(text=f"{file.read()}")
        else:
                messagebox.showinfo("Внимание!","Вы ввели не правильный путь к файлу!")
        file.close()

text_2 = Label(tab_3, text="Введите путь к файлу из которого надо импортировать текст")
text_2.place(x=28, y=0)


input_path=Entry(tab_3,font=("Roboto",10), width=10)
input_path.place(x = 30, y=20)

button = Button(tab_3, text="кнопка",font=("Roboto", 8),command=import_text)
button.place(x=120, y=20)
# D:\text.txt
root.mainloop()