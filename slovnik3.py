"""Simple dictionary to store data in key-value format"""
import os
from tkinter import messagebox, simpledialog, Label, Button, \
    Checkbutton, Menu, IntVar, Message, Tk, END
from ttkwidgets.autocomplete import AutocompleteCombobox  # pip install ttkwidgets
import pyttsx3

engine = pyttsx3.init()  # инициализация движка
engine.setProperty('rate', 200)  # скорость речи
engine.setProperty('volume', 1)  # громкость

with open('dict.txt', 'r+') as f:
    dict_temp = {}
    for line in f.readlines():
        line = line.strip()
        k = line.split(' ')[0]
        v = line.split(' ')[1]
        dict_temp[k] = v


def get_key():
    """generates a list of keys"""
    keys_temp = []
    for key in dict_temp.keys():
        keys_temp.append(key)
    return keys_temp


def add_word(user_word):
    """adds new word in dictionary"""
    user_translate = simpledialog.askstring('OK', f'translate: {user_word}')
    if user_translate is None:
        wrong_value()
    else:
        dict_temp[user_word] = user_translate
        with open('dict.txt', 'a') as file:
            file.write(user_word + ' ' + user_translate + '\n')


def wrong_value():
    """error message for wrong value"""
    messagebox.showerror('Info', 'wrong value')


def exit_program():
    """confirmation message for exit"""
    choice = messagebox.askyesno('Quit', 'Do you want to exit?')
    if choice:
        window.destroy()


def clear_input():
    """clears the input line of Combobox"""
    key_word.delete(0, END)
    key_word.focus()


def say_message(message):
    """voice translation"""
    engine.say(message)
    engine.runAndWait()


def info():
    """text in Menu-info message"""
    label_info['text'] = 'Слова хранятся в файле dict.txt'


def trans():
    """translates input word (if translation available) or prompts to enter translate"""
    user_word = key_word.get().lower()
    if user_word.isalpha():  # проверка на отсутствие цифр
        if user_word in get_key():
            message = dict_temp[user_word]
            out_box['text'] = message
            if say_var.get():  # проверка галочки say!
                say_message(message)
        else:
            add_word(user_word)
    else:
        wrong_value()


def open_google():
    """open Google translator (En-Ru)"""
    os.system("start https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate")


window = Tk()
window.title('Slovnik')
window.geometry('440x250+150+100')
window.resizable(False, False)  # запрет растягивать в высоту и длину
say_var = IntVar()  # определение галочки say!

label = Label(text='enter word or choose..', bg='#bdeb34', font='Consolas 11')
label.place(relx=0.02, rely=0.05)
button1 = Button(text='Translate', command=trans, font='Consolas 11')
button1.place(x=340, y=90, width=90, height=35)
button2 = Button(text='Clear', command=clear_input, font='Consolas 11')
button2.place(x=340, y=130, width=90, height=35)
button3 = Button(text='ask Google', command=open_google, font='Consolas 11')
button3.place(x=230, y=130, width=90, height=35)
button4 = Button(text='Quit', command=exit_program, font='Consolas 11')
button4.place(x=340, y=170, width=90, height=35)
checkbutton = Checkbutton(text='Say!', font='Consolas 11', variable=say_var)
checkbutton.place(x=250, y=90, width=50, height=35)

out_box = Label(text='', font='Consolas 11')
out_box.place(x=230, y=40, width=200, height=35)
out_box['bg'] = 'white'

key_word = AutocompleteCombobox(window, completevalues=get_key(), font='Consolas 11')
key_word.postcommand = get_key()    # обновляет список при добавлении слова
key_word.place(x=10, y=40, width=200, height=35)
key_word.focus()

menu = Menu(window)  # window это главное окно
submenu = Menu(window, tearoff=0)  # tearoff убираем штриховую инию
window.config(menu=menu)

submenu.add_command(label='Info', command=info)
submenu.add_command(label='Quit', command=exit_program)
menu.add_cascade(label='Info', menu=submenu)

label_info = Message()
label_info.place(x=10, y=90, width=150, height=95)

window.mainloop()
