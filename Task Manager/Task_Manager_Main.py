from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import json


customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("light")
window = customtkinter.CTk()
window.title("To Do List App")
window.geometry("350x600")
window.resizable(FALSE, FALSE)
window.iconbitmap("tasks.ico")

def add_new_task_to_list():
    task = add_task_entry.get()
    # Load existing tasks from the JSON file
    with open("tasks.json", mode="r") as f:
        data = json.load(f)
    # Append the new task to the existing list
    data.append(task)
    # Write the updated task list back to the JSON file
    with open("tasks.json", mode="w") as f:
        json.dump(data, f)
    # Add the new task to the GUI list
    task_list.insert(END, task)
    add_task_entry.delete(0, END)

def clear_tasks():
    # Clear the existing tasks in the JSON file
    with open("tasks.json", mode="w") as f:
        json.dump([], f)
    # Clear the GUI list
    task_list.delete(0, END)

def delete_task():
    # Get the index of the selected task in the GUI list
    selection = task_list.curselection()
    if len(selection) == 0:
        CTkMessagebox.show("No task selected")
        return
    index = selection[0]
    # Load existing tasks from the JSON file
    with open("tasks.json", mode="r") as f:
        data = json.load(f)
    # Remove the selected task from the existing list
    del data[index]
    # Write the updated task list back to the JSON file
    with open("tasks.json", mode="w") as f:
        json.dump(data, f)
    # Remove the selected task from the GUI list
    task_list.delete(index)

# Welcome text
welcome_text = customtkinter.CTkLabel(window, text="Your daily tasks")
welcome_text.place(x=125, y=20)

# Add task entry
add_task_entry = customtkinter.CTkEntry(
    window, 
    placeholder_text="Add Quick Task...", 
    width=200, 
    height=25, 
    border_width=2, 
    corner_radius=10
)
add_task_entry.place(x=20, y=50)

# Add quick task button
add_task_button = customtkinter.CTkButton(
    window, 
    text='Add Quick Task', 
    command=add_new_task_to_list, 
    width=32, 
    height=20
)
add_task_button.place(x=235, y=52)

# Clear Task Button
edit_task_button = customtkinter.CTkButton(
    window, 
    text="Clear Tasks", 
    width=30, 
    command=clear_tasks
)
edit_task_button.place(x=50, y=530)

# Delete Task Button
delete_task_button = customtkinter.CTkButton(
    window, 
    text="Delete Task", 
    width=30, 
    command=delete_task
)
delete_task_button.place(x=220, y=530)

# Task List

try:
    with open("tasks.json", mode="r") as f:
        data = json.load(f)
except json.decoder.JSONDecodeError:
    data = []

task_list = Listbox(window, height=25, width=40, font=("helvetica", 25, "normal"))

# Populate the task list with the tasks from the JSON file
for task in data:
    task_list.insert(END, task)

task_list.place(x=70, y=290)

### New Task Window ###


window.mainloop()
