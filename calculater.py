
from tkinter import *

def number_press(num):
    global equation_text
    equation_text= equation_text + str(num)
    equation_lable.set(equation_text)
def equal():

    global equation_text
    try:
        total=str(eval(equation_text))
        equation_lable.set(total)
        equation_text=total
    except SyntaxError:
        equation_lable.set('SyntaxError')
        equation_text=''
    except ZeroDivisionError:
        equation_lable.set('ZeroDivisionError')
        equation_text=''
    
def clear():
    global equation_text

    equation_lable.set('')
    equation_text=''
def backspace():
    global equation_text
      
    equation_text=equation_text[:-1]
    equation_lable.set(equation_text)
    

    
    

window=Tk()
window.title('CALCULATOR')
window.geometry('500x500')
equation_text=''
equation_lable=StringVar()
label=Label(window,textvariable=equation_lable,font=('arieal',20),bg='white',width=26,height=3)
label.pack()

frame=Frame(window)
frame.pack()

button1=Button(frame,text='1',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(1))
button1.grid(row=0,column=0)

button2=Button(frame,text='2',font=('areal',10),width=6,height=3,bg='white',fg='black',command=lambda:number_press(2))
button2.grid(row=0,column=1)

button3=Button(frame,text='3',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(3))
button3.grid(row=0,column=2)

button4=Button(frame,text='4',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(4))
button4.grid(row=1,column=0)

button5=Button(frame,text='5',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(5))
button5.grid(row=1,column=1)

button7=Button(frame,text='7',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(7))
button7.grid(row=2,column=0)

button6=Button(frame,text='6',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(6))
button6.grid(row=1,column=2)

button8=Button(frame,text='8',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(8))
button8.grid(row=2,column=1)

button9=Button(frame,text='9',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(9))
button9.grid(row=2,column=2)

button0=Button(frame,text='0',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press(0))
button0.grid(row=3,column=1)



add=Button(frame,text='+',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press('+'))
add.grid(row=0,column=3)
minus=Button(frame,text='-',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press('-'))
minus.grid(row=1,column=3)
multy=Button(frame,text='*',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press('*'))
multy.grid(row=2,column=3)
divison=Button(frame,text='/',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=lambda: number_press('/'))
divison.grid(row=3,column=3)

equall=Button(frame,text='=',font=('arieal',10),width=6,height=3,bg='white',fg='green',command=equal)
equall.grid(row=3,column=2)

back=Button(frame,text='<--',font=('arieal',10),width=6,height=3,bg='white',fg='black',command=backspace)
back.grid(row=3,column=0)

clears=Button(window,text='clear',font=('arieal',10),width=9,height=3,bg='white',fg='black',command=clear)
clears.pack()

window.mainloop()