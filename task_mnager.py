import tkinter as tk
from tkinter import messagebox

# Create main app class
class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Task Manager")
        #self.geometry("300x400")

        # Title Label
        self.title_label = tk.Label(self, text="Task Manager", font=("Arial", 16))
        self.title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

        # Task Entry Field
        self.task_entry = tk.Entry(self, width=25, font=("Arial", 12))
        self.task_entry.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

        # Button to add task
        self.add_button = tk.Button(self, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.grid(row=3,column=0,padx=10,pady=10)

        # Task List Box
        self.task_listbox = tk.Listbox(self, width=30, height=5, font=("Arial", 12))
        self.task_listbox.grid(row=5,column=0,padx=10,pady=10)

        # Buttons for actions (Delete, Mark Done)
        self.delete_button = tk.Button(self, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_button.grid(row=4,column=0,sticky='e',padx=10,pady=10)

        self.done_button = tk.Button(self, text="Mark as Done", font=("Arial", 12), command=self.mark_done)
        self.done_button.grid(row=4,column=0,sticky='w',padx=10,pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)  # Add task to the listbox
            self.task_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{task} (Done)")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Running the app
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
