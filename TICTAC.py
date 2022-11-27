
from tkinter import *
import random

def newgame():
    pass



window=Tk()
window.title('TIC-TAC-TOE')
players=['x','o']
player=random.choice(players)
buttons=[[0,0,0],
        [0,0,0],
        [0,0,0]]

label=Label(text=player+'  Turn',font=('arial',40))
label.pack(side='top')

reset_buttom=Button(text='Restart',font=('arial',25),command=newgame)
reset_buttom.pack()

frame=Frame(window)
frame.pack()

for row in range (3):
    for column in range (3):
        buttons[row][column]=Button(frame,text='',font=('arial',25),width=5,height=2, 
                                        command= lambda row=row,column=column:newgame(row,column))

        buttons[row][column].grid(row=row,column=column)
window.mainloop()