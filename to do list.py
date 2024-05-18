import tkinter as tk
from tkinter import messagebox

# Create the main application window with an orange background
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg='#FF8324')  # Orange background

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root, bg='#FF8324')  # Match frame background color to main window
frame.pack(pady=10)

# Listbox to display tasks with light teal background
task_listbox = tk.Listbox(
    frame,
    width=50,
    height=15,
    selectmode=tk.SINGLE,
    bg='#BBE3DA',  # Set background color to light teal
    fg='black'     # Set foreground color to black
)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Entry widget to add a new task
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Buttons to add and delete tasks with teal background and white text
add_task_button = tk.Button(root, text="Add Task", command=add_task, bg='#009C9A', fg='white')
add_task_button.pack(pady=10)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, bg='#009C9A', fg='white')
delete_task_button.pack(pady=10)

# Run the main loop
root.mainloop()

