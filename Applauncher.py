import tkinter as t
from tkinter import filedialog, Text 
import os

root = t.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    filePath = filedialog.askopenfilename(initialdir="/", title="Select App",
    filetypes=(("Applications", "*.exe"),("All Files","*.*")))
    
    apps.append(filePath)
    
    for app in apps:
        label = t.Label(frame, text=app, bg="yellow")
        label.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)

canvas = t.Canvas(root, height=700, width=700, bg="#C96567")
canvas.pack()

frame = t.Frame(root, bg="white") 
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)

chooseFile = t.Button(root, text="Choose App", padx=10, pady=5, fg="black", bg="#C96567", command=addApp)
chooseFile.pack()

launch = t.Button(root, text="Launch Apps", padx=10, pady=5, fg="black", bg="#C96567", command=runApps)
launch.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop() 

with open('savedPaths.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')