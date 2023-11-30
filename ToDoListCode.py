# Importing the necessary modules
import tkinter as tk
from datetime import datetime

# Defining a class named TodoApp
class TodoApp:
    # Initializing the class with the root window as a parameter
    def __init__(self, root):
        # Setting up the root window
        self.root = root
        self.root.title("To-Do App")

        # Initializing variables and configuring background color
        self.tasks = []
        self.task_var = tk.StringVar()
        self.priority_var = tk.StringVar(value="Medium")
        self.root.configure(bg="#00008B")  # Set background color to blue

        # Creating Entry widget for entering tasks
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Creating a Label widget for displaying "Priority:"
        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.grid(row=0, column=1, padx=10, pady=10)

        # Creating an OptionMenu widget for selecting task priority
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "High", "Medium", "Low")
        self.priority_menu.grid(row=0, column=2, padx=10, pady=10)

        # Creating a Button widget for adding tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        # Creating a Listbox widget for displaying the list of tasks
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Creating a Button widget for marking tasks as complete
        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Creating an Entry widget for filtering tasks
        self.filter_entry = tk.Entry(root, width=30)
        self.filter_entry.grid(row=2, column=1, padx=10, pady=10)

        # Creating a Button widget for applying task filtering
        self.filter_button = tk.Button(root, text="Filter", command=self.filter_tasks)
        self.filter_button.grid(row=2, column=2, padx=10, pady=10)

    # Method for adding a new task to the list
    def add_task(self):
        task = self.task_var.get()
        priority = self.priority_var.get()
        if task:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            task_with_info = f"{task} (Priority: {priority}, Added on: {timestamp})"
            # Insert the task in a sorted manner based on priority
            index = 0
            for existing_task in self.tasks:
                existing_priority = existing_task.split("(Priority: ")[1][0]
                if priority <= existing_priority:
                    break
                index += 1
            self.tasks.insert(index, task_with_info)
            self.update_task_list()
            self.task_var.set("")

    # Method for marking a task as complete
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])
            self.update_task_list()

    # Method for filtering tasks based on a keyword
    def filter_tasks(self):
        keyword = self.filter_entry.get().lower()
        filtered_tasks = [task for task in self.tasks if keyword in task.lower()]
        self.update_task_list(filtered_tasks)

    # Method for updating the task list in the GUI
    def update_task_list(self, tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks = tasks or self.tasks
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
