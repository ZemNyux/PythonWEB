import sys
import ctypes

# не потрібно встановлювати окрему бібліотеку для Tkinter через pip install —
# це стандартна бібліотека Python

if sys.platform.startswith("win"):
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 0
    )

import tkinter as tk
from controller import TaskController

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskController(root)
    root.mainloop()