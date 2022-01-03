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

song_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=(
    "arial", 15), height=12, width=47, selectbackground="gray", selectforeground="black")

song_list.grid(columnspan=9)

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
previous_button = Button(root, text="Previous", width=7, command=Previous)
previous_button.grid['font'] = defined_font
previous_button.grid(row=1, column=4)

# Next Button
next_button = Button(root, text="Next", width=7, command=Next)
next_button.grid['font'] = defined_font
next_button.grid(row=1, column=5)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()


# Function to play the song

# Adding many songd to Playlist

def addsongs():

    # Open a file dialog

    temp_song = filedialog.askopenfilenames(initialdir="/home/downloads/music",
                                            title="Select a Song", filetypes=(("mp3 Files", "*.mp3"),))

    # Add the song to the listbox

    for song in temp_song:
        song = song.replace("/home/downloads/music/", "")
        song_list.insert(END, song)


def deletesong():
    # Delete the selected song from the listbox

    curr_song = song_list.curselection()
    song_list.delete(curr_song[0])


def Play():
    song = song_list.get(ACTIVE)
    song = f"/home/downloads/music/{song}"
    mixer.music.load(song)
    mixer.music.play()

# Function to pause the song


def Pause():
    mixer.music.pause()

# Function to resume the song


def Resume():
    mixer.music.unpause()


# Function to stop the song

def Stop():
    mixer.music.stop()
    song_list.selection_clear(ACTIVE)

# Navigate from the Current Song


def Previous():
    previous_song = song_list.curselection()

    # Previous song index

    previous_song = previous_song[0] - 1

    # Get Previous song

    temp2 = song_list.get(previous_song)
    temp2 = f"/home/downloads/music/{temp2}"

    mixer.music.load(temp2)
    mixer.music.play()
    song_list.selection_clear(0, END)

    # Activate New Song
    song_list.activate(previous_song)

    # Set Next Song

    song_list.selection_set(previous_song)


def Next():
    next_song = song_list.curselection()

    # Next song index

    next_song = next_song[0] + 1

    # Get Next song

    temp2 = song_list.get(next_song)
    temp2 = f"/home/downloads/music/{temp2}"

    mixer.music.load(temp2)
    mixer.music.play()
    song_list.selection_clear(0, END)

    # Activate New Song
    song_list.activate(next_song)

    # Set Next Song

    song_list.selection_set(next_song)
