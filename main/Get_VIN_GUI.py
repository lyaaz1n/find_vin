# -*- coding: utf-8 -*-
"""
@author: a.lyzin
"""
import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter import ttk
import re
import os
import pandas as pd
import time


def click():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    name = " output.xlsx"
    savefile = timestr + name
    default_dir = r'C:\Users\a.lyzin\Downloads'
    save_dir = os.path.join(default_dir, savefile)
    file_path = tkinter.filedialog.askopenfilename (title = 'выбрать файл', initialdir = (os.path.expanduser (default_dir)))
    try:
        df = pd.read_excel(file_path)
        
        df['VIN'] = ""
        #df['VIN'] = df['Назначение платежа']
        
        vins = []
        for index, row in df.iterrows():
           cel = row['Назначение платежа']
           vin = re.findall(r'\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+', cel) 
           vin = re.sub(r"[а-яА-Я]+","", cel)
    
           vin = re.findall(r'\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+\w+', vin)
           vins.append(vin)
        
        df['VIN'] = vins
        df['VIN'] = df['VIN'].str.get(0)
    
        df.to_excel(save_dir, index = False)
        tkinter.messagebox.showinfo(title = 'Статус', message = 'Файл в папке Загрузки')
    except:
        tkinter.messagebox.showerror(title = 'Статус', message = 'Ошибка')
    return df
    
    
root = Tk()
root.title("выбор файла")
root.geometry('500x200')

canvas = Canvas(root, height=150, width=100)
canvas.pack()

frame = Frame(root,bg="grey")
frame.pack()

title = Label(frame, text='Выбери файл и файл с VIN сохраниться у Тебя в папке загрузки', bg = 'red')
title.pack()
btn = Button(frame, text='выбери файл', command = click)
btn.pack()

root.mainloop()

