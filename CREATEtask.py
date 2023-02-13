import tkinter as tk
import tkinter.messagebox
from tkinter import VERTICAL
from tkinter import HORIZONTAL
from tkinter import RIGHT
from tkinter import LEFT
from tkinter import Y
from tkinter import X
from tkinter import ACTIVE


#initialize window
window = tk.Tk()
window.title("To Do App by alancward")
window.geometry("300x280")
window.configure(bg='#D4F8FF')
window.resizable(False, False)
tasks = []

#functions
def ClearText():
    TaskEntry.delete(0, tkinter.END)

def AddTask():
    task = TaskEntry.get()
    tasks.append(task)
    
    if task != " ":
        TasksBox.insert(tkinter.END, task)

        ClearText()
    else:
        tkinter.messagebox.showwarning(title="Invalid Input", message = "You must enter a task.")
def DeleteTask():
    TaskPosition = TasksBox.curselection()[0]
    TasksBox.delete(TaskPosition)

def StarTask():
    TaskPosition = TasksBox.curselection()[0]
    x = TaskPosition
    y = "*" + " " + tasks[x]
    TasksBox.delete(TaskPosition)
    TasksBox.insert(TaskPosition, y)



def DeleteAll(listlen):
    for i in range(listlen):
        TasksBox.delete(0)
def ClearListBox():
    DeleteAll(len(tasks))
#GUI
TasksFrame = tkinter.Frame(window)
TasksFrame.pack(side=LEFT)


#List of tasks inputted
TasksBox = tkinter.Listbox(window, height=10, width=50)
TasksBox.pack()

#Scroll Bar     
TaskScrollbarY = tkinter.Scrollbar(TasksFrame, orient=VERTICAL, command=TasksBox.yview)
TaskScrollbarY.pack(side=LEFT, fill=Y)


#Task Entry Widget
TaskEntry = tkinter.Entry(window, width=50)
TaskEntry.pack()

#Task Deletion Button
TaskDelete = tkinter.Button(window, bg="white" , text= "Delete Task", width=48, command=DeleteTask)
TaskDelete.pack()
#Add TaskEntry value to list 
AddButton = tkinter.Button(window, bg="white", text="Add Task", width=48, command=AddTask)
AddButton.pack()
#Add a star indicating importance of task
TaskStar = tkinter.Button(window, bg="white", text="Important Task", width=48, command=StarTask)
TaskStar.pack()
#Delete All Tasks button
TaskDeleteAll = tkinter.Button(window, bg="white", text="Delete All Tasks", width= 48, command=ClearListBox)
TaskDeleteAll.pack()


#Return & Backspace used for addition/deletion of tasks
window.bind("<Return>",lambda x: AddTask())
window.bind("<BackSpace>", lambda x: DeleteTask())



window.mainloop()