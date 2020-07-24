import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.title('Burgess Technology Name Picker v1.0')

HEIGHT = 700
WIDTH = 700
GRAY = '#292929'
DARKGRAY = '#32322F'
LIGHTGRAY = '#828282'
LIGHTGREEN = '#a6cc54'
RED='#eb4034'

LIST_OF_EMPLOYEES = ['Andrew','Anthony','Ben','Cynthia','Daniel','Doug','Jeanne', 'Jennifer', 'Josh', 'Julie', 'Justin', 'Logan', 'Maggie','Matt','Micah','Mike','Norm','Tamara','Tom']

list_of_names = []

def complete(event):
    winner = random.choice(list_of_names)
    
    label13 = tk.Label(frame3, text='The Winner is: ' + winner, bg='white', fg='black', font=("Helvetica", 11))
    label13.pack()
    list_of_names.remove(winner)

def enter_name(event):
    global label12
    n = 0
    name_event = name_entry.get()
    list_of_names.append(name_event)
    label12 = tk.Label(frame2, text=list_of_names[-1], bg='white', fg='black',font=("Helvetica", 7))
    label12.pack(side='top')
    n+=1
    frame2.forget()

    name_entry.delete(0, END)

    if len(list_of_names) >= 22:
        name_entry.forget()

def auto_enter(event):
    global label12
    n=0
    for name in LIST_OF_EMPLOYEES:
        list_of_names.append(name)
        label12 = tk.Label(frame2, text=list_of_names[-1], bg='white', fg='black',font=("Helvetica", 7))
        label12.pack(side='top')
        n+=1
        frame2.forget()
    button3['state'] = DISABLED

def clear_all(event):
    for widget in frame2.winfo_children():
        widget.destroy()

    for widget in frame3.winfo_children():
        widget.destroy()

    for names in list_of_names:
        list_of_names.clear()

    button3['state'] = NORMAL

def clear_last():
    label12.destroy()
    list_of_names.pop()
    enter_name(event)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=GRAY)
canvas.pack()

frame = tk.Frame(root,bg=DARKGRAY)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

frame2 = tk.Frame(root, bg='white')                               #bottom Left
frame2.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.5)

label_a = tk.Label(frame, text='--- Names in the Hat ---', bg=DARKGRAY, fg=LIGHTGREEN, font=("Helvetica", 12))
label_a.place(relx=0.04, rely=.325)

label_b = tk.Label(frame, text='--- Winners ---', bg=DARKGRAY, fg=LIGHTGREEN, font=("Helvetica", 12))
label_b.place(relx=0.73, rely=.325)

frame3 = tk.Frame(root, bg='white')                                  # Bottom Right
frame3.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.5)

label = tk.Label(frame, bg=DARKGRAY, text='-- Enter Names Here --', fg='white', font=("Helvetica", 13))
label.pack(side='top')

name_entry = tk.Entry(frame, bg='white')
name_entry.bind('<Return>', enter_name)
name_entry.pack(side='top')

labelb = tk.Label(frame, bg=DARKGRAY)                                # Spacer
labelb.pack(side='top')

button_ca = tk.Button(frame, text='Remove Last Name', command=clear_last)
button_ca.pack()

button2 = tk.Button(frame, text='Generate Random Winner', bg=LIGHTGREEN)
button2.bind('<Button-1>', complete)
button2.pack(side='top')

button3 = tk.Button(frame, text='Add Entire Staff')
button3.bind('<Button-1>', auto_enter)
button3.place(relx=0.42, rely=.6)

button4 = tk.Button(frame, text='Clear All', bg=RED)
button4.bind('<Button-1>', clear_all)
button4.place(relx=0.45, rely=.9)


root.mainloop()
