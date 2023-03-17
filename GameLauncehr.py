import tkinter as tk
import subprocess
from tkinter import *
import webbrowser
import sys
import os

usersettings = r'C:\Users\Kiman\Downloads\KanaLauncher\UserSettings.txt'

# Create the main window
window = tk.Tk()
window.geometry("600x900")
window.title("Kana Launcher")
logo = PhotoImage(file=r'C:\Users\Kiman\Downloads\KanaLauncher\krnlll.png')
window.wm_iconphoto(True, logo) 


with open(usersettings) as f:
  lines = f.readlines()

#================================================================================================================

def open_Fortnite():

  os.startfile(#enter dir)

def open_roblox():

  os.startfile(#enter dir))

def open_overwatch():

  os.startfile(#enter dir))

def open_r6():
  os.startfile(#enter dir))


#====================================================================================================

def open_sp():

  os.startfile(#enter dir))

def open_discord():

  os.startfile(#enter dir))

def open_vsc():

  os.startfile(#enter dir)")

def open_ubisoft():

  os.startfile(#enter dir))

def open_battlenet():
  os.startfile(#enter dir))

def open_4anime():

  webbrowser.open_new_tab("4anime.gg/")

def fps():
  os.startfile(#enter dir))

def bm():
  os.startfile(#enter dir))

def tModLoader():
  os.startfile(#enter dir))

def commandpanel():
  newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
  newWindow.title("UserSettings.Conf")
 
    # sets the geometry of toplevel
  newWindow.geometry("500x500")
 
    # A Label widget to show in toplevel
  Label(newWindow,
        text =(lines)).pack()

#============================================================================================================

frame = LabelFrame(text="  Frequent Games     ", padx=125, pady=15)
frame.pack()

# Create the button
button0 = tk.Button(frame, text="Open Fortnite", command=open_Fortnite)

button1 = tk.Button(frame, text="Open Overwatch", command=open_overwatch)

button2 = tk.Button(frame, text="Open Roblox", command=open_roblox)

button3 = tk.Button(frame, text="Open Apex Legends", command=open_r6)

button4 = tk.Button(frame, text="Open tModLoader", command=tModLoader)

button0.grid(row=1, column=2, pady=15)

button1.grid(row=3, column=2, pady=20)

button2.grid(row=6, column=2, pady=23)

button3.grid(row=9, column=2, pady=27)

button4.grid(row=11, column=2, pady=31)
#================================================================================================

frame2 = LabelFrame(text="  Frequent Applications  ", padx=125, pady=15)
frame2.pack()

# Create the button
button0 = tk.Button(frame2, text="Open Spotify", command=open_sp)

button1 = tk.Button(frame2, text="Open Visual Studio", command=open_vsc)

button2 = tk.Button(frame2, text="Open Ubisoft Connect", command=open_ubisoft)

button4 = tk.Button(frame2, text="Open Battle.net", command=open_battlenet)

button3 = tk.Button(frame2, text="Open 4Anime", command=open_4anime)

button5 = tk.Button(frame2, text="Open Discord", command=open_discord)

button0.grid(row=1, column=2, pady=15)

button1.grid(row=3, column=2, pady=20)

button2.grid(row=6, column=2, pady=23)

button3.grid(row=9, column=2, pady=25)

button4.grid(row=12, column=2, pady=27)

button5.grid(row=14, column=2, pady=29)

#================================================================================================

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Settings', menu=filemenu)
filemenu.add_separator()

#================================================================================================

submenu = Menu()

submenu.add_command(label="FPS Unlocker [ROBLOX]", command=fps)
submenu.add_command(label="BakkesMod [RL]", command=bm)

#================================================================================================

filemenu.add_cascade(label="3rd Party Software", menu=submenu)
filemenu.add_command(label='Exit', command=window.quit)
filemenu.add_separator()
filemenu.add_command(label="[const.release]", command=commandpanel)
filemenu.add_separator()

#================================================================================================

window.mainloop()
