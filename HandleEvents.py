from tkinter import *
from PIL import ImageTk, Image


def click_chess_event(event):
    img = ImageTk.PhotoImage(Image.open("cam.jpg"))  # PIL solution
    event.widget.create_image(30, 30, image=img)
    event.widget.image = img




def key(event):
    print("pressed", repr(event.char))
