import tkinter as tk
import subprocess
from tkinter import *
import webbrowser
import sys
import os

window = tk.Tk()
window.geometry("500x200")
window.title("menu startfile")
logo = PhotoImage(file=#enter dir for logo image')
window.wm_iconphoto(True, logo) 

def open_launcher():
    os.startfile(#enter dir for GameLauncehr.py")

def open_speedtest():
    os.startfile(#enter dir for speedtest.py")

frame = LabelFrame(text="      Types      ", padx=125, pady=15)
frame.pack()

button0 = tk.Button(frame, text="Open Games Launcher [v2.7.1]", command=open_launcher)

button1 = tk.Button(frame, text="Open Speed Test [v1.0]", command=open_speedtest)

button0.grid(row=1, column=2, pady=15)

button1.grid(row=3, column=2, pady=20)

window.mainloop()
