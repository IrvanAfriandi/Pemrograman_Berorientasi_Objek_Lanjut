import pygame
from tkinter import *
pygame.init()


animal_sounds = ['Anjing.mp3', 'Babi.mp3', 'Bebek.mp3', 'Burung Hantu.mp3', 'Domba.mp3', 'Kelelawar.mp3', 'Kodok.mp3', 'Lumba Lumba.mp3', 'Macan.mp3', 'Sapi.mp3']
def play_sound(animal):
    pygame.mixer.music.load(animal)
    pygame.mixer.music.play()

root = Tk()
root.title("Aplikasi Suara Hewan")
root.geometry('300x450+500+100')

for i in range(len(animal_sounds)):
    button = Button(root, text=animal_sounds[i][:-4], command=lambda animal=animal_sounds[i]: play_sound(animal))
    button.pack(pady=7, padx=0)

root.mainloop()
pygame.quit()
