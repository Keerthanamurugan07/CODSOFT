import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Frame for input and buttons
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5)

        # Add Task Button
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, width=10)
        self.add_button.grid(row=0, column=1, padx=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(master, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(padx=10, pady=5)

        # Delete Task Button
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, width=10)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
