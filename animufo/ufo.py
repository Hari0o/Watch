import tkinter
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='D://python practice//animufo//city.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='D://python practice//animufo//spider.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

photo_image2 = PhotoImage(file='D://python practice//animufo//VENOM.png')
my_image2 = canvas.create_image(0,500,image=photo_image2,anchor=NE)

image_width = photo_image.width()
image_height = photo_image.height()

image_width1 = photo_image2.width()
image_height1 = photo_image2.height()

while True:
    coordinates = canvas.coords(my_image)
    # print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)

    if(coordinates[0]>=(WIDTH-image_width1) or coordinates[0]<0):
        xVelocity = xVelocity
    if(coordinates[1]>=(HEIGHT-image_height1) or coordinates[1]<0):
        yVelocity = yVelocity

    canvas.move(my_image2,-xVelocity,-yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()

