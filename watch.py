from tkinter import *
from time import *

def update():

    clock= strftime('%I:%M:%S  %p')
    timelable.config(text=clock)

    day=strftime('%A')
    daylable.config(text=day)

    date=strftime('%d %b %Y')
    datelable.config(text=date)

    window.after(1000,update)



window = Tk()

timelable=Label(window,font=('arial',20),fg='red',bg='white')
timelable.pack()

daylable=Label(window,font=('arial',20),fg='red',bg='white')
daylable.pack()

datelable=Label(window,font=('arial',20),fg='red',bg='white')
datelable.pack()

update()

window.mainloop()

# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)

#     day_string = strftime("%A")
#     day_label.config(text=day_string)

#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)

#     window.after(1000,update)


# window = Tk()

# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()


# update()

# window.mainloop()

