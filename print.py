import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
result_path = filedialog.askdirectory()
path = Path(file_path).glob("**/*.png")

startX = 138
startY = 120
stepX = 731
stepY = 1086
marginX = 5
marginY = 5

files = []
for file in path:
    files.append(file)
for i in range(0, len(files), 9):
    back = Image.open('./back.png') # type: Image
    bback = Image.open('./bb.png') # type: Image
    
    for x in range(0,3):
        for y in range(0,3):
            currentI = i+x*3+y
            if currentI < len(files):
                current = Image.open(files[currentI])
                resized = current.resize((stepX, stepY))
                back.paste(resized, (startX+(marginX+stepX)*x, startY+(marginY+stepY)*y))
    back.save(result_path+'/print_'+str(i)+'.png')
    bback.save(result_path+'/back_'+str(i)+'.png')

# area = (40, 1345, 551, 1625)
# im1.paste(im2, area)
