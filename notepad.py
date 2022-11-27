import os
from tkinter import *
from tkinter import colorchooser,font,filedialog
from tkinter.messagebox import *
from tkinter.filedialog import*

def colour_chooserfg():
    colour=colorchooser.askcolor()
    text_area.config(fg=colour[1])
def colour_chooserbg():
    colour=colorchooser.askcolor()
    text_area.config(bg=colour[1])

def text():
    pass
def change_font(*args):
    text_area.config(font=(font_name.get(),font_size.get()))
def save_file():
    file=filedialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',
                                        filetypes=[('all files','*.*'),('text document','*.txt')])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file=open(file,'w')

            file.write(text_area.get(1.0,END))
        except Exception:
            print('cant read file')
        finally:
            file.close()

def open_file():
    file=askopenfilename(defaultextension='.txt',file=[('All Files','*.*'),('Text Documents','*.txt')])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0,END)

        file=open(file,'r')
        text_area.insert(1.0, file.read())

    except Exception:
        print('wrong file')

    finally:
        file.close()
def new_file():
    window.title('Untitle')
    text_area.delete(1.0,END)
def cut():
    text_area.event_generate('<<Cut>>')
def paste():
    text_area.event_generate('<<Paste>>')
def copy():
    text_area.event_generate('<<Copy>>')
def quit():
    window.destroy()
def about():
    showinfo('Notepad', 'YOU CAN WRITE')

window= Tk()
window.title('NOTEPAD')
File=None
window_width= 500
window_height = 500
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

window.geometry('{}x{}+{}+{}'.format(window_width,window_height,x,y))

font_name=StringVar()
font_name.set('Arial')

font_size=StringVar()
font_size.set('25')

text_area=Text(window,font=(font_name.get(),font_size.get()))

scrool_bar=Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+S+E+W)
scrool_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scrool_bar.set)

frame=Frame(window)
frame.grid()

colour_choose=Button(frame,text='colour',command=colour_chooserfg)
colour_choose.grid(row=0,column=0)
colour_choose1=Button(frame,text='colourbg',command=colour_chooserbg)
colour_choose1.grid(row=0,column=3)


fontsize=Spinbox(frame,from_=1,to=100,command=change_font,textvariable=font_size)
fontsize.grid(row=0,column=4)


fontname=OptionMenu(frame,font_name,*font.families(),command=change_font)
fontname.grid(row=0,column=2)

menu_bar=Menu(window)
window.config(menu=menu_bar)

file_name=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=file_name)
file_name.add_command(label='New',command=new_file)
file_name.add_command(label='Open',command=open_file)
file_name.add_command(label='Save',command=save_file)
file_name.add_separator()
file_name.add_command(label='Quit',command=quit)

edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut',command=cut)
edit_menu.add_command(label='Copy',command=copy)
edit_menu.add_command(label='Paste',command=paste)

help_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='About',command=about)








window.mainloop()