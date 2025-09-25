from tkinter import *
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✅ To-Do List")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f8ff")

        self.tasks = []

        # ---------------- Title ----------------
        title = Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#4682b4", fg="white")
        title.pack(fill=X)

        # ---------------- Input Frame ----------------
        input_frame = Frame(root, bg="#f0f8ff")
        input_frame.pack(pady=10)

        self.task_entry = Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.pack(side=LEFT, padx=5)

        add_btn = Button(input_frame, text="Add Task", command=self.add_task, bg="#4caf50", fg="white")
        add_btn.pack(side=LEFT, padx=5)

        # ---------------- Listbox for tasks ----------------
        self.task_listbox = Listbox(root, width=45, height=10, font=("Arial", 12), selectmode=SINGLE, bg="white")
        self.task_listbox.pack(pady=10)

        # ---------------- Button Frame ----------------
        btn_frame = Frame(root, bg="#f0f8ff")
        btn_frame.pack(pady=10)

        del_btn = Button(btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", width=12)
        del_btn.grid(row=0, column=0, padx=5)

        clr_btn = Button(btn_frame, text="Clear All", command=self.clear_all, bg="#ff9800", fg="white", width=12)
        clr_btn.grid(row=0, column=1, padx=5)

        exit_btn = Button(btn_frame, text="Exit", command=root.quit, bg="black", fg="white", width=12)
        exit_btn.grid(row=0, column=2, padx=5)

    # --------------- Functions ---------------
    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showerror("Input Error", "Task cannot be empty!")
            return
        self.tasks.append(task)
        self.update_listbox()
        self.task_entry.delete(0, END)

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            del self.tasks[selected]
            self.update_listbox()
        except IndexError:
            messagebox.showerror("Delete Error", "Please select a task to delete")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Do you really want to clear all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(END, f"{i}. {task}")


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = Tk()
    app = TodoApp(root)
    root.mainloop()
