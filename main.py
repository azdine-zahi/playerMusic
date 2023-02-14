from tkinter import *
import pygame
from PIL import Image, ImageTk
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import random

# ---------------------------- Initialize Pygame ----------------------- #

root = Tk()
root.title("Music Player")
root.geometry("600x400")
root.configure(bg='#5E5E5E')

# Initialize Pygame Mixer
pygame.mixer.init()

# ---------------------------- Functions ------------------------------- #

# Status Bar
def play_time():

    # Check for Double Timing
    if stopped:
        return

    # Time Elapsed
    current_time = pygame.mixer.music.get_pos() / 1000
    
    # Slider Label to enable slider to move
    # slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')

    # Convert Time To Time Format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # Get Currently Playing Song
    # current_song = song_box.curselection() # returns a tuple
    
    # Add One To The Current Song Number
    song = song_box.get(ACTIVE)
    
    # Add Directory Structure + Song Title To Find Song File
    song = f'musiques/{song}.mp3'

    # Load Song With Mutagen
    song_mut = MP3(song)

    # Get Song Length
    global song_length
    song_length = song_mut.info.length

    # Convert To Time Format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    
    # Increase Current Time By One Second
    current_time += 1

    # Check To See If Song Has Ended
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length} of {converted_song_length} ')

    elif int(my_slider.get()) == int(current_time):
        # Update Slider To Position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    
    elif paused:
        pass
    
    else:
        # Update Slider To Position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        
        # Convert Time To Time Format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

        # Output Time To Status Bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')  

        # Move Slider Along By One Second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # Output Time To Status Bar
    # status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')
    
    # Update Slider Position Value To Current Song Position
    # my_slider.config(value=int(current_time))

    # Update Time Every Second
    slider_position = int(song_length)
    
    # update slider to position
    my_slider.config(to=slider_position, value=int(current_time))

    # Update Time Every Second
    status_bar.after(1000, play_time)


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="audio/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    # Strip out the directory info and .mp3 extension from the song name and add it to the listbox
    song = song.replace("musiques/", "")
    song = song.replace(".mp3", "")
    
    # add song to listbox
    song_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="audio/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    # Loop through song list and replace directory info and mp3 extension
    for song in songs:
        song = song.replace("musiques/", "")
        song = song.replace(".mp3", "")
        
        # add song to listbox
        song_box.insert(END, song)


# Delete A Song
def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop


# Delete All Songs
def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop


# Play Selected Song
def play():
    # Set Stopped Variable To False So Song Can Play
    global stopped
    stopped = False 
    song = song_box.get(ACTIVE)
    song = f'musiques/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Call The Status Bar Function To Get Song Length
    play_time()

    # # Update Slider To Position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # # Update volume value
    # current_volume = pygame.mixer.music.get_volume()


# Stop Playing Current Song
def stop():

    # Reset Slider Position and Status Bar
    status_bar.config(text='')
    my_slider.config(value=0)

    # Stop Song From Playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Clear Status Bar
    status_bar.config(text='')

    # Set Stop variable to True
    global stopped
    stopped = True

# Create Global Pause Variable
global paused
paused = False


def next_song():
    # Reset Slider Position and Status Bar
    status_bar.config(text='')
    
    # Set Slider To Zero
    my_slider.config(value=0)
    
    # Get Current Song Number
    next_one = song_box.curselection() # returns a tuple
    
    # Add One To The Current Song Number
    next_one = next_one[0] + 1
    
    # Grab Song Title From Playlist
    song = song_box.get(next_one)
    
    # Add Directory Structure + Song Title To Find Song File
    song = f'musiques/{song}.mp3'
    
    # Load And Play Song With Pygame Mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear Active Bar In Playlist
    song_box.selection_clear(0, END)
    
    # Move Active Bar To Next Song
    song_box.activate(next_one)
    
    # Set Active Bar To Next Song
    song_box.selection_set(next_one, last=None)


def previous_song():
    # Reset Slider Position and Status Bar
    status_bar.config(text='')

    # Set Slider To 0
    my_slider.config(value=0)

    # Get Current Song Number
    next_one = song_box.curselection() # returns a tuple

    # Add One To The Current Song Number
    next_one = next_one[0] - 1

    # Grab Song Title From Playlist
    song = song_box.get(next_one)

    # Add Directory Structure + Song Title To Find Song File
    song = f'musiques/{song}.mp3'

    # Load And Play Song With Pygame Mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear Active Bar In Playlist
    song_box.selection_clear(0, END)

    # Move Active Bar To Next Song
    song_box.activate(next_one)
    
    # Set Active Bar To Next Song
    song_box.selection_set(next_one, last=None)


# Pause and Unpause Current Song
def pause(is_paused):
    global paused
    paused = is_paused
    
    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True


# Create Slider Function
def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'musiques/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    
    # get current volume
    # current_volume = pygame.mixer.music.get_volume()
    # volume_label.config(text=f'Volume: {int(current_volume * 100)}%')


def repeat():
    # Set Stopped Variable To False So Song Can Play
    global stopped
    stopped = False 
    song = song_box.get(ACTIVE)
    song = f'musiques/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=-1)
    
    # Call The Status Bar Function To Get Song Length
    play_time()

    # # Update Slider To Position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)


def random_song():
    # Reset Slider Position and Status Bar
    status_bar.config(text='')
    
    # Set Slider To 0
    my_slider.config(value=0)
    
    # Get Current Song Number
    next_one = song_box.curselection() # returns a tuple
    
    # Add One To The Current Song Number
    next_one = random.randint(0, len(song_box)-1)
    
    # Grab Song Title From Playlist
    song = song_box.get(next_one)
    
    # Add Directory Structure + Song Title To Find Song File
    song = f'musiques/{song}.mp3'
    
    # Load And Play Song With Pygame Mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear Active Bar In Playlist
    song_box.selection_clear(0, END)
    
    # Move Active Bar To Next Song
    song_box.activate(next_one)
    
    # Set Active Bar To Next Song
    song_box.selection_set(next_one, last=None)


# ---------------------------- GUI -------------------------------- #

# -----------------------------Frames------------------------------ #

# Create Main Frame
master_frame = Frame(root, bg='#5E5E5E')
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="white", width=75, selectbackground="light gray", selectforeground="black")
song_box.grid(row=0, column=0)

# Create Player Control Frame
controls_frame = Frame(master_frame, bg='#5E5E5E' )
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Frame
volume_frame = LabelFrame(master_frame, text="Volume", bg='#5E5E5E')
volume_frame.grid(row=0, column=1, padx=20)

# -----------------------------Buttons----------------------------- #

# Backward Button
back_btn_img = Image.open("images/previous-track.png")
back_btn_img.thumbnail((50, 50))
back_btn_img = ImageTk.PhotoImage(back_btn_img)

# Forward Button
forward_btn_img = Image.open("images/next-track.png")
forward_btn_img.thumbnail((50, 50))
forward_btn_img = ImageTk.PhotoImage(forward_btn_img)

# Play Button
play_btn_img = Image.open("images/play-button.png")
play_btn_img.thumbnail((50, 50))
play_btn_img = ImageTk.PhotoImage(play_btn_img)

# Pause Button
pause_btn_img = Image.open("images/pause-track.png")
pause_btn_img.thumbnail((50, 50))
pause_btn_img = ImageTk.PhotoImage(pause_btn_img)

# Stop Button
stop_btn_img = Image.open("images/stop-button.png")
stop_btn_img.thumbnail((50, 50))
stop_btn_img = ImageTk.PhotoImage(stop_btn_img)

# Random
random_btn_img = Image.open("images/shuffle.png")
random_btn_img.thumbnail((40, 40))
random_btn_img = ImageTk.PhotoImage(random_btn_img)

# Repeat
repeat_btn_img = Image.open("images/repeat-track.png")
repeat_btn_img.thumbnail((40, 40))
repeat_btn_img = ImageTk.PhotoImage(repeat_btn_img)


# Create Player Control Buttons
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, bg='#5E5E5E', command = previous_song)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, bg='#5E5E5E', command = next_song)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, bg='#5E5E5E', command = play)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, bg='#5E5E5E', command = lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, bg='#5E5E5E', command = stop)
repeat_btn = Button(controls_frame, image=repeat_btn_img, borderwidth=0, bg='#5E5E5E', command = repeat)
random_btn = Button(controls_frame, image=random_btn_img, borderwidth=0, bg='#5E5E5E', command = random)


# Grid Player Control Buttons
back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)
repeat_btn.grid(row=0, column=5, padx=10)
random_btn.grid(row=0, column=6, padx=10)


#-----------------------------Menu--------------------------------- #

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdown
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command = add_song)

# Add Many Songs To Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command = add_many_songs)

# Create Delete Song Menu Dropdown
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Selected Song From Playlist", command = delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command = delete_all_songs)

#-----------------------------Status Bar---------------------------- #

# Create Status Bar To Bottom Of App
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

#-----------------------------Sliders------------------------------- #

# Create Slider For Time Song Position
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command = slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10, padx=20)

# Create Slider Label
# slider_label = Label(root, text='0:00')
# slider_label.pack(pady=10)

root.mainloop()