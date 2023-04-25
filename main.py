import tkinter as tk
from tkinter import messagebox



class ToDoList:
    def __init__(self, master):
        "This is the to-do list class"

        self.master = master
        master.title("To-Do List")

        self.task_label = tk.Label(master, text="Enter task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_list = tk.Listbox(master)
        self.tasks_list.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.create_delete_button()

    def create_delete_button(self):
        if not hasattr(self, 'delete_button'):
            self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_task)
            self.delete_button.pack()

    def delete_task(self):
        selection = self.tasks_list.curselection()
        if selection:
            self.tasks_list.delete(selection[0])
        if self.tasks_list.size() == 0:
            self.delete_button.pack_forget()
            del self.delete_button

root = tk.Tk()
root.geometry("400x300")
app = ToDoList(root)
root.mainloop()