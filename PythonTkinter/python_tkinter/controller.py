from model import TaskModel
from view import TkView


class TaskController:
    def __init__(self, root):
        self.model = TaskModel()
        self.view = TkView(root, self) # передаємо root і себе (controller)

    def run(self):
        # у Tkinter запуск через mainloop, тому run не потрібен
        pass