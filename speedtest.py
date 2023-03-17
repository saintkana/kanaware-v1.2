import tkinter as tk
import subprocess
from tkinter import *
import webbrowser
import sys
import os
import speedtest as speedtest

window = tk.Tk()
window.geometry("600x850")
window.title("Speedtest")
logo = PhotoImage(file=() #import file directory
window.wm_iconphoto(True, logo)

speed_test = speedtest.Speedtest()
download_speed = speed_test.download()
upload_speed = speed_test.upload()
speed_test.get_best_server()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

def uploadpeed_changed():
    label0.config(text=download_speed)

download_speed = bytes_to_mb(speed_test.download())
 
label0 = tk.Label(text=" Upload Speed :")         # Label Text
label0.pack()

tk.mainloop()
