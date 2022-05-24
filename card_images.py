from tkinter import *
from PIL import ImageTk, Image

from config import card_images

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage


def load_images():
    """load all the card images into an array with id's corresponding to card numbers"""
    card_images.append(PhotoImage(file="cards/ace_of_spades.png"))
    card_images.append(PhotoImage(file="cards/ace_of_spades.png"))
    card_images.append(PhotoImage(file="cards/2_of_spades.png"))
    card_images.append(PhotoImage(file="cards/3_of_spades.png"))
    card_images.append(PhotoImage(file="cards/4_of_spades.png"))
    card_images.append(PhotoImage(file="cards/5_of_spades.png"))
    card_images.append(PhotoImage(file="cards/6_of_spades.png"))
    card_images.append(PhotoImage(file="cards/7_of_spades.png"))
    card_images.append(PhotoImage(file="cards/8_of_spades.png"))
    card_images.append(PhotoImage(file="cards/9_of_spades.png"))
    card_images.append(PhotoImage(file="cards/10_of_spades.png"))
    card_images.append(PhotoImage(file="cards/jack_of_spades.png"))
    card_images.append(PhotoImage(file="cards/queen_of_spades.png"))
    card_images.append(PhotoImage(file="cards/king_of_spades.png"))

    card_images.append(PhotoImage(file="cards/ace_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/2_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/3_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/4_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/5_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/6_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/7_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/8_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/9_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/10_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/jack_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/queen_of_hearts.png"))
    card_images.append(PhotoImage(file="cards/king_of_hearts.png"))

    card_images.append(PhotoImage(file="cards/ace_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/2_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/3_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/4_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/5_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/6_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/7_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/8_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/9_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/10_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/jack_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/queen_of_diamonds.png"))
    card_images.append(PhotoImage(file="cards/king_of_diamonds.png"))

    card_images.append(PhotoImage(file="cards/ace_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/2_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/3_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/4_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/5_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/6_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/7_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/8_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/9_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/10_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/jack_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/queen_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/king_of_clubs.png"))
    for i in range(0, 53):
        card_images[i] = resizeImage(card_images[i], 98, 143)
