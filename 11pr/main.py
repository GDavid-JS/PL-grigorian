from tkinter import *
import requests
import json

root = Tk()
root.title("Григорян Давид Жирайрович")
root.geometry("500x500")
root.resizable(False, False)
root["bg"] = "#555"

def processing_json(user_data):
    return {
        'company': user_data.get('company'),
        'created_at': user_data.get('created_at'),
        'email': user_data.get('email'),
        'id': user_data.get('id'),
        'name': user_data.get('name'),
        'url': user_data.get('login')
    }

def get_json(name):
    url = f"https://api.github.com/users/{name}"
    return requests.get(url).json()

def create_json(user_data, name):
    json_file = open(f"{name}.json", "w")
    json.dump(user_data, json_file)

# Создаем json с моим вариантом
def first_task():
    user_data = get_json('nixpkgs')
    create_json(user_data, 'nixpkgs_data')

# Выполняем поиск по имени репозитория
def second_task():
    user_data = get_json(inputLink.get())
    processing_user_data = processing_json(user_data)

    create_json(processing_user_data, 'data_file')

first_task()

inputLink = Entry(font=("Roboto",13))
inputLink.place(x=20, y=20, height=30, width=150)

button = Button(text="Кнопка",font=("Roboto",14), bg='#fff',command=second_task)
button.place(x=190, y=20, height=40)


root.mainloop()