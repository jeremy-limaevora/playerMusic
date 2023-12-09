from tkinter import *
from pygame import mixer
import os
from tkinter import filedialog
import pygame

looping= False 

def play_music():
    current_song = playlist.curselection()
    if current_song:
        index = current_song[0]
        song = playlist.get(index)
        mixer.music.load(song)
        mixer.music.play(loops=-1 if looping else 0)
       

def pause_music():
    mixer.music.pause()

def stop_music():
    mixer.music.stop()

def resume_music():
    mixer.music.unpause()

def volume_music(valeur):
    volume= float(valeur) / 100
    mixer.music.set_volume(volume)

def ajouter_music():
    files= filedialog.askopenfilenames(filetypes=[("MP3 files","*.mp3")])
    for file in files:
        playlist.insert(END, file)

def réecouter_music():
    global looping
    looping = not looping
    réecouter_music_button.config(text="lecture en boucle:ON" if looping else "lecture en boucle: OFF")
    
def music_end_event():
    if looping:
       play_music()
    else:
       mixer.music.stop()
       
USEREVENT = pygame.USEREVENT + 1

def prochaine_piste():
    current_index = playlist.curselection()
    if current_index:
        next_index = current_index[0] + 1
        if next_index < playlist.size():
            playlist.selection_clear(0, END)
            playlist.selection_set(next_index)
            playlist.activate(next_index)
            play_music()

def piste_précedente():
    current_index = playlist.curselection()
    if current_index:
        previous_index = current_index[0] - 1
        if previous_index >= 0:
            playlist.selection_clear(0, END)
            playlist.selection_set(previous_index)
            playlist.activate(previous_index)
            play_music()


    


mixer.init()

root = Tk()
root.title('Lecteur de Media')



playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('Arial', 15), width=40)
playlist.grid(columnspan=5)

music_folder = "music"  
music_files = [file for file in os.listdir(music_folder) if file.endswith('.mp3')]

for file in music_files:
    playlist.insert(END, os.path.join(music_folder, file))

play_button = Button(root, text="Play", command=play_music)
play_button.grid(row=1, column=0)

pause_button = Button(root, text="Pause", command=pause_music)
pause_button.grid(row=1, column=1)

stop_button = Button(root, text="Stop", command=stop_music)
stop_button.grid(row=1, column=2)

resume_button = Button(root, text="Reprendre", command=resume_music)
resume_button.grid(row=1, column=3)

volume_button = Scale (root, from_=0,to=100, orient=HORIZONTAL, command=volume_music)
volume_button.set(50)
volume_button.grid(row=2, column=3,rowspan=4)

ajouter_music_button = Button(root, text="ajouter piste", command= ajouter_music)
ajouter_music_button.grid(row=2, columnspan=2,column=0)

réecouter_music_button = Button(root, text= "lecture en boucle:OFF", command=réecouter_music)
réecouter_music_button.grid(row=1, column= 4)

next_button = Button(root, text=">>", command=prochaine_piste)
next_button.grid(row=3, column=4)

previous_button = Button(root, text="<<", command=piste_précedente)
previous_button.grid(row=3, column=1)


mixer.music.set_endevent(USEREVENT)
root.bind(USEREVENT, lambda e: music_end_event())





root.mainloop()


