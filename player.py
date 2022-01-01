# Import Libraries (Dependencies)

from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

# Creating the Root Window

root = Tk()
root.title("CodeIt Music Player")

# Initialize Mixer

mixer.init()

# Listbox containing the songs

song_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", width=50, height=20, font=("arial", 15),
                    height=12, width=47, selectbackground="gray", selectforeground="black")

song_list.grid(columnsoan=9)

# Button font

defined_font = font.Font(family='Helvetica')

# Play Button
play_button = Button(root, text="Play", width=7, command=Play)
play_button.grid['font'] = defined_font
play_button.grid(row=1, column=0)

# pause button

pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button.grid['font'] = defined_font
pause_button.grid(row=1, column=1)

# Stop button

stop_button = Button(root, text="Stop", width=7, command=Stop)
stop_button.grid['font'] = defined_font
stop_button.grid(row=1, column=2)

# Resume Button

Resume_button = Button(root, text="Resume", width=7, command=Resume)
Resume_button.grid['font'] = defined_font
Resume_button.grid(row=1, column=3)

# Previous Button
