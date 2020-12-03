import shutil
import glob
import time
import os
import subprocess
import tkinter as tk

print("Scripting App - Lance M. Peterson")

src = "C:/Users/Lance.Peterson/Desktop/Scripting/Parker"
dst1 = "C:/Users/Lance.Peterson/Desktop/Scripting/Parker/ServicesResult"
dst2 = "C:/Users/Lance.Peterson/Desktop/Scripting/Parker/AppsResult"

EXTENSIONS = ('txt')

root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 350, height = 250) 
canvas1.pack()

def start_batch(): 
    subprocess.call([r'C:/Users/Lance.Peterson/Desktop/Scripting/Parker/BatchScripts/parkerRunWorkout.bat'])

def check_services():
    subprocess.call([r'C:/Users/Lance.Peterson/Desktop/Scripting/Parker/BatchScripts/parkerCheckServices.bat'])
    shutil.move(src=src + "/ServicesResult.txt", dst=dst1)
	
def check_apps():
    subprocess.call([r'C:/Users/Lance.Peterson/Desktop/Scripting/Parker/BatchScripts/parkerCheckApps.bat'])
    shutil.move(src=src + "/currentApps.png", dst=dst2)
	    
button1 = tk.Button (root, text='Run Workout ',command=start_batch,bg='green',fg='white')
button2 = tk.Button (root, text='Check Services ',command=check_services,bg='green',fg='white')
button3 = tk.Button (root, text='Check Apps ',command=check_apps,bg='green',fg='white')
canvas1.create_window(170, 90, window=button1)
canvas1.create_window(170, 130, window=button2)
canvas1.create_window(170, 170, window=button3)

root.mainloop()
	
input("Press Enter to continue...")