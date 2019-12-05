import tkinter as tk
from tkinter import filedialog
from PIL import Image


root = tk.Tk()
root.withdraw()

oldPath = filedialog.askdirectory()
newPath = filedialog.askdirectory()

changes = filedialog.askopenfiles()

for change in changes:
    old = Image.open(oldPath+change.name)
    new = Image.open(newPath+change.name)
