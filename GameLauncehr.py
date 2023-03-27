# saintkana (sora)
# My Github: https://https://github.com/saintkana

#================================================================================================================
#                                                 Importing Required Libraries
#================================================================================================================


import tkinter as tk
import subprocess
from tkinter import *
import webbrowser
import sys
import os

#================================================================================================================
#                                                 Main Window Features/Settings
#================================================================================================================

window = tk.Tk()

window.geometry("600x900") #Geometry (Meaning Size)
window.title("Kana Launcher")
logo = PhotoImage(file=r'')  # add the directory for your logo.
window.wm_iconphoto(True, logo) 

#================================================================================================================
#                                                 Defining VisualBasicScript Errors
#================================================================================================================

def readerrormessage():
  os.startfile(r'') # add the directory for the VisualBasicScript Error Message File

def steamerror():
  os.startfile(r'') # add the directory for the steam error VisualBasicScript File

#================================================================================================================
#                                                 Defining Game Directories (dir)
#================================================================================================================

def open_Fortnite():

  readerrormessage() # add the directory for Fortnite

def open_roblox():

  os.startfile(r'') # add the directory for ROBLOX

def open_overwatch():

 readerrormessage() # OR add the directory for Overwatch

def open_r6():

  steamerror() # OR add the directory for Rainbow Six Siege


#================================================================================================================
#                                               Defining Miscelaneous Directories (dir)
#================================================================================================================


def open_sp():

  os.startfile(r'') # add the directory for Spotify

def open_discord():

  os.startfile(r'') # add the directory for discord

def open_vsc():

  os.startfile(r'') # add the directory for 

def open_ubisoft():

  readerrormessage()

def open_battlenet():

  readerrormessage()

def open_zoroto():

  webbrowser.open_new_tab("zoro.to/")

def fps():
  
  steamerror()

def bm():

  steamerror()

def tModLoader():
  
  steamerror()

def commandpanel():
  newWindow = Toplevel(window)

  newWindow.title("UserSettings.Conf")
 
  newWindow.geometry("500x500")
 
  lines = r'' # add the directory for usersettings.txt
  Label(newWindow, text=(lines)).pack()

#================================================================================================================
#                               Creating the Frame and Buttons and adding their Assigned Commands (1/2) (Tkinter)
#================================================================================================================

frame = LabelFrame(text="   Frequent Games     ",
                    padx=125, pady=15)
frame.pack()

# Create the button
button0 = tk.Button(frame, text="Open Fortnite",
                     command=open_Fortnite)

button1 = tk.Button(frame, text="Open Overwatch",
                     command=open_overwatch)

button2 = tk.Button(frame, text="Open Roblox",
                     command=open_roblox)

button3 = tk.Button(frame, text="Open Apex Legends",
                     command=open_r6)

button4 = tk.Button(frame, text="Open tModLoader",
                     command=tModLoader)

button0.grid(row=1, column=2, pady=15)

button1.grid(row=3, column=2, pady=20)

button2.grid(row=6, column=2, pady=23)

button3.grid(row=9, column=2, pady=27)

button4.grid(row=11, column=2, pady=31)

#================================================================================================================
#                               Creating the Frame and Buttons and adding their Assigned Commands (2/2) (Tkinter)
#================================================================================================================

frame2 = LabelFrame(text="  Frequent Applications  ",
                     padx=125, pady=15)
frame2.pack()

# Create the button
button0 = tk.Button(frame2, text="Open Spotify",
                     command=open_sp)

button1 = tk.Button(frame2, text="Open Visual Studio",
                     command=open_vsc)

button2 = tk.Button(frame2, text="Open Ubisoft Connect",
                     command=open_ubisoft)

button4 = tk.Button(frame2, text="Open Battle.net",
                     command=open_battlenet)

button3 = tk.Button(frame2, text="Open 4Anime", 
                    command=open_zoroto)

button5 = tk.Button(frame2, text="Open Discord",
                     command=open_discord)

button0.grid(row=1,
              column=2, 
                pady=15)

button1.grid(row=3,
              column=2,
                pady=20)

button2.grid(row=6,
              column=2,
                pady=23)

button3.grid(row=9, 
             column=2,
               pady=25)

button4.grid(row=12,
              column=2,
                pady=27)

button5.grid(row=14,
              column=2, 
                pady=29)

#================================================================================================================
#                                               Creating the Dropdown Menu (Tkinter)
#================================================================================================================

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu,
                 tearoff=False)

menu.add_cascade(label='Settings',
                  menu=filemenu)

filemenu.add_separator()

#================================================================================================

submenu = Menu()
submenu.add_separator()

submenu.add_command(label="FPS Unlocker [ROBLOX]",
                     command=fps)

submenu.add_command(label="BakkesMod [RL]",
                     command=bm)

submenu.add_separator()

#================================================================================================

filemenu.add_cascade(label="3rd Party Software",
                      menu=submenu)

filemenu.add_command(label='Exit',
                      command=window.quit)

filemenu.add_separator()

filemenu.add_command(label="[const.release]",
                      command=commandpanel)

filemenu.add_separator()

#================================================================================================================
#                                               Tkinter MainLoop (Tkinter)
#================================================================================================================

window.mainloop()
