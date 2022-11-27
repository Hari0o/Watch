from tkinter import *
import time

def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		hours, mins = divmod(mins, 60)
		days, hours = divmod(hours, 24)
		timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs) 
		
		print(timer,end='\r')
		time.sleep(1)
		t+=1
	time_label.config(text=timer)
	print('timer completed')
t=input('enter the time in seconds: ')

countdown(int(t))

window=Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

countdown(t)


window.mainloop()
