import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from wand.image import Image
from psd_tools import PSDImage
from PIL import Image as PILImage

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

path = Path(file_path)

for file in path.glob("**/*.txt"):
    base = os.path.splitext(str(file))[0]
    os.rename(str(file), base + ".psd")

for file in path.glob("**/*.psd"):
    print(file)
    psd = Image(filename=file)
    base = os.path.splitext(str(file))[0]
    print(psd)
    with psd.convert('png') as converted:
        Image(image=converted.sequence[0]).save(filename=base+".png")