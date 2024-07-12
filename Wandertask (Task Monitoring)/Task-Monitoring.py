#Prerequisite Libraries:
#Pillow   (py -m pip install Pillow)
#tkcalendar   (py -m pip install tkcalendar)


import tkinter
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pickle

window = Tk()
window.title("TASK MONITOR")
window.geometry('700x560')
window.config(bg="#2f2e2c")
window.resizable(0, 0)
#window.iconbitmap("ICON.ICO")

# REMOVING TITLE BAR
window.overrideredirect(True)

#FUNCTIONS OF TITLE BAR
def move_app(e):  # runs when window is dragged
    window.geometry(f'+{e.x_root}+{e.y_root}')

def quitter(e):
    window.quit()

def mo(e):
    close_label['background'] = 'red'

def Lmo(e):
    close_label['background'] = '#2f2e2c'

def mo2(e):
    min_label['background'] = 'red'

def Lmo2(e):
    min_label['background'] = '#2f2e2c'

def min(e):
    window.withdraw()
    window.overrideredirect(FALSE)
    window.iconify()

# CREATE A NEW TITLE BAR
title_bar = Frame(window, bg="#f8de7e", relief="ridge", bd=2)
title_bar.pack(side=TOP, fill=BOTH)
title_bar.bind("<B1-Motion>", move_app)


#TITLE BAR LABEL
title_label0 = Label(title_bar, text="  📝 ", font=("Arial", 18),bg="#f8de7e", fg="#000000")
title_label0.pack(side=LEFT, padx=2)
title_label = Label(title_bar, text="WANDERTASK:", font=("Arial", 14, "bold"),bg="#f8de7e", fg="#000000")
title_label.pack(side=LEFT, pady=4, padx=1)
title_label2 = Label(title_bar, text="WHERE PRODUCTIVITY PEAKS", font=("Arial", 12),bg="#f8de7e", fg="#000000")
title_label2.pack(side=LEFT, pady=4, padx=3)

#TITLE BAR CLOSE
close_label = Label(title_bar, text=" x ",font=("Arial", 11), bg="#2f2e2c", fg='#f8de7e', relief="raised")
close_label.pack(side=RIGHT,padx=4, pady=4, ipady=1 )
close_label.bind("<Button-1>", quitter)
close_label.bind("<Enter>", mo)
close_label.bind("<Leave>", Lmo)

#TITLE BAR MINIMIZE
min_label = Label(title_bar, text="-", font=("Arial", 11), bg="#2f2e2c", fg="#f8de7e", relief="raised")
min_label.pack(side = RIGHT, padx=4, pady=4, ipadx=4, ipady=1)
min_label.bind("<Button-1>", min)

min_label.bind("<Enter>", mo2)
min_label.bind("<Leave>", Lmo2)

# LOGO
image = Image.open("WANDERTASK_LOGO.png")
resize_image = image.resize((400, 65))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.place(x=161, y=55)


#ADD BUTTON
def add_task():
    babe = cat_list.get()
    baby = task_entry.get()
    mahal = date_cal.get()
    if babe != "":
        List_task1.insert(END, babe)
        task_entry.delete(0, "end")

        if baby != "":
            List_task2.insert(END, baby)
            cat_list.delete(0, "end")

            if mahal != "":
                List_task3.insert(END, mahal)
                date_cal.delete(0, "end")

    else:
        messagebox.showwarning("warning", "Please enter some task.")

#DELETE BTN
def del_task():
    try:
        task_index = List_task3.curselection()
        for task_index  in task_index[::-1]:
            List_task3.delete(task_index)

            task_index = List_task2.curselection()
            for task_index in task_index[::-1]:
                List_task2.delete(task_index)

            task_index = List_task1.curselection()
            for task_index in task_index[::-1]:
                List_task1.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

#CLEAR INPUT TASK
def input_del():
    cat_list.delete(0,END)
    task_entry.delete(0,END)
    date_cal.delete(0,END)

#INPUT & DELETE COLOR
def hold(e):
    btn_del2['background'] = 'red'
def leave(e):
    btn_del2['background'] = '#f8de7e'

#SAVE LIST
def save_tasks():
    tasks1 = List_task1.get(0, List_task1.size())
    tasks2 = List_task2.get(0, List_task2.size())
    tasks3 = List_task3.get(0, List_task3.size())
    pickle.dump(tasks1, open("tasks1.dat", "wb"))
    pickle.dump(tasks2, open("tasks2.dat", "wb"))
    pickle.dump(tasks3, open("tasks3.dat", "wb"))

#LOAD LIST
def load_tasks():
    try:
        tasks1 = pickle.load(open("tasks1.dat", "rb"))
        List_task1.delete(0, tkinter.END)
        List_task2.delete(1, tkinter.END)
        List_task3.delete(2, tkinter.END)
        for task in tasks1:
            List_task1.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

    try:
        tasks2 = pickle.load(open("tasks2.dat", "rb"))
        List_task2.delete(0, tkinter.END)
        for task in tasks2:
            List_task2.insert(tkinter.END, task)

    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

    try:
        tasks3 = pickle.load(open("tasks3.dat", "rb"))
        List_task3.delete(0, tkinter.END)
        for task in tasks3:
            List_task3.insert(tkinter.END, task)

    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

#CATEGORY LIST (ENTRY)
def cat():
    cat_list["values"] = ["CPEN60",
                          "PHYS14",
                          "DCEE21",
                          "MATH12",
                          "FITT2",
                          "GNED02",
                          "GNED12", ]


cat_list = ttk.Combobox(window, values=["CPEN60",
                                        "PHYS14",
                                        "DCEE21",
                                        "MATH12",
                                        "FITT2",
                                        "GNED02",
                                        "GNED12", ], font=("Arial", 12), width=13, postcommand=cat)
cat_list.place(x=18, y=140)

lbl2 = Label(window, text = "CATEGORY ", fg="black", bg="#f8de7e", font=("Arial", 12,"bold"), width= 13)
lbl2.place(x=16,y=210)

#SCROLLBAR TO MULTIPLE LISTBOXES
def scroll(*args):
    List_task1.yview(*args)
    List_task2.yview(*args)
    List_task3.yview(*args)

#CHANGING COLORS OF BUTTONS
def on_enter(e):
    btn_del['background'] = 'red'
def on_leave(e):
    btn_del['background'] = '#f8de7e'

def on_enter1(e):
    btn_add['background'] = 'white'
def on_leave1(e):
    btn_add['background'] = '#f8de7e'

def on_enter2(e):
    btn_save['background'] = 'white'
    btn_save['foreground'] = "#2f2e2c"
def on_leave2(e):
    btn_save['background'] = "#2f2e2c"
    btn_save['foreground'] = '#f8de7e'
def on_enter3(e):
    btn_load['background'] = 'white'
    btn_load['foreground'] = "#2f2e2c"
def on_leave3(e):
    btn_load['background'] = "#2f2e2c"
    btn_load['foreground'] = '#f8de7e'

#ENTRY_TASK
task_entry = Entry(window,font=("Arial",13), bd= 1, width=45)
task_entry.place(x=160,y=140)
lbl1 = Label(window, text = "TASK NAME ", fg="black", bg="#f8de7e", font=("Arial", 12,"bold"), width=40)
lbl1.place(x=158,y=210)

#ENTRY_DATE
lbl3 = Label(window, text = "DUE DATE ", fg="black", bg="#f8de7e", font=("Arial", 12,"bold"),width=11)
lbl3.place(x=571,y=210)
#date label
date_cal = DateEntry(window,bd=1, width=10, year=2022, month=6, day=1,justify="center", font=12,
background='#1E4558', foreground='white', borderwidth=2)
date_cal.place(x=571, y=140)

#LIST BOX1
List_task1 = tkinter.Listbox(window, height= 19, width= 23,justify="center",exportselection="False",selectmode=MULTIPLE)
List_task1.place(x=15, y= 240)

#LIST BOX2
List_task2 = tkinter.Listbox(window, height= 19, width= 69,justify="center",exportselection="False",selectmode=MULTIPLE)
List_task2.place(x=154, y= 240)

#LIST BOX3
List_task3 = tkinter.Listbox(window, height= 19, width= 19,justify="center",exportselection="False",selectmode=MULTIPLE)
List_task3.place(x=568, y= 240)

#SCROLLBAR SETTINGS
scrollbary = tk.Scrollbar(window,orient=tk.VERTICAL, command=scroll)
List_task1.config(yscrollcommand=scrollbary.set)
List_task2.config(yscrollcommand=scrollbary.set)
List_task3.config(yscrollcommand=scrollbary.set)
scrollbary.place(x=670, y=240,height=308, width=17)

#LOAD BTN
btn_load = tkinter.Button(title_bar, text="Load",font=("Arial", 8), width=4,bg="#2f2e2c", fg="#f8de7e",command=(load_tasks))
btn_load.bind("<Enter>", on_enter3)
btn_load.bind("<Leave>", on_leave3)
btn_load.pack(side = RIGHT, padx=1, pady=4, ipadx=3)

#SAVE BTN
btn_save = tkinter.Button(title_bar, text="Save", font=("Arial", 8), width=4,bg="#2f2e2c", fg="#f8de7e",command=save_tasks)
btn_save.bind("<Enter>", on_enter2)
btn_save.bind("<Leave>", on_leave2)
btn_save.pack(side = RIGHT, padx=3, pady=4, ipadx=3)

#ADD BTN
btn_add = tkinter.Button(window, text="Add", width=5, command=add_task,bg="#f8de7e")
btn_add.place(x=20, y=170)
btn_add.bind("<Enter>", on_enter1)
btn_add.bind("<Leave>", on_leave1)

#CLEAR INPUT BTN
btn_del2 = tkinter.Button(window, text="Clear Inputs", width=9,command=input_del,bg="#f8de7e")
btn_del2.place(x=611, y=170)
btn_del2.bind("<Enter>", hold)
btn_del2.bind("<Leave>", leave)

#DELETE BTN
btn_del = tkinter.Button(window, text="Delete", width=5,command=del_task,bg="#f8de7e")
btn_del.place(x=69, y=170)
btn_del.bind("<Enter>", on_enter)
btn_del.bind("<Leave>", on_leave)


window.mainloop()
