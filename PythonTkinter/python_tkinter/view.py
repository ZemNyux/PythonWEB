import tkinter as tk
from tkinter import messagebox, ttk
from typing import List
from model import Task


class TkView:
    def __init__(self, root: tk.Tk, controller):
        self.root = root
        self.controller = controller
        self.root.title("Список завдань")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # стилі
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10))
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))

        # верхня частина - додавання завдання
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Опис завдання:", font=("Segoe UI", 11)).pack(side="left", padx=(0, 10))

        self.entry = ttk.Entry(top_frame, font=("Segoe UI", 11), width=50)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.focus_set()

        add_btn = ttk.Button(top_frame, text="Додати", command=self.add_task, style="Accent.TButton")
        add_btn.pack(side="right", padx=(10, 0))

        # список завдань
        self.tree = ttk.Treeview(root, columns=("№", "Статус", "Опис"), show="headings", height=15)
        self.tree.heading("№", text="№", anchor="center")
        self.tree.heading("Статус", text="Статус", anchor="center")
        self.tree.heading("Опис", text="Опис", anchor="w")

        self.tree.column("№", width=50, anchor="center")
        self.tree.column("Статус", width=80, anchor="center")
        self.tree.column("Опис", width=450, anchor="w")

        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # кнопки дій
        btn_frame = ttk.Frame(root, padding=10)
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="Позначити як виконане", command=self.mark_done).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Видалити", command=self.delete_task).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Оновити", command=self.refresh).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Вихід", command=root.quit).pack(side="right", padx=5)

        # прив'язка Enter до додавання
        self.entry.bind("<Return>", lambda e: self.add_task())

        self.refresh()

    def add_task(self):
        desc = self.entry.get().strip()
        if not desc:
            messagebox.showwarning("Помилка", "Опис не може бути порожнім!")
            return

        if self.controller.model.add_task(desc):
            self.entry.delete(0, tk.END)
            self.refresh()
            messagebox.showinfo("Успіх", "Завдання додано!")
        else:
            messagebox.showerror("Помилка", "Щось пішло не так...")

    def mark_done(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Увага", "Виберіть завдання!")
            return

        item = self.tree.item(selected[0])
        idx = int(item["values"][0]) - 1

        if self.controller.model.mark_done(idx):
            self.refresh()
            messagebox.showinfo("Успіх", "Завдання позначено як виконане!")
        else:
            messagebox.showerror("Помилка", "Невірний індекс")

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Увага", "Виберіть завдання!")
            return

        item = self.tree.item(selected[0])
        idx = int(item["values"][0]) - 1

        if messagebox.askyesno("Підтвердження", "Видалити це завдання?"):
            if self.controller.model.delete_task(idx):
                self.refresh()
                messagebox.showinfo("Успіх", "Завдання видалено!")
            else:
                messagebox.showerror("Помилка", "Невірний індекс")

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks: List[Task] = self.controller.model.get_all_tasks()
        if not tasks:
            self.tree.insert("", "end", values=("", "[Список порожній]", ""))
            return

        for i, task in enumerate(tasks, 1):
            status = "✓" if task.done else "—"
            tag = "done" if task.done else "pending"
            self.tree.insert("", "end", values=(i, status, task.description), tags=(tag,))

        self.tree.tag_configure("done", foreground="green")
        self.tree.tag_configure("pending", foreground="gray")