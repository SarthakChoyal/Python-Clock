from tkinter import *

from time import strftime

root = Tk()
root.title('Clock.exe')


def display_time():
    c_time= strftime('%I:%M:%S %p')
    label_time.config(text=c_time)
    label_time.after(1000,display_time)


label_time= Label(root,text='Time',font=('Helvecta',60), bg='black', fg='cyan' )
label_time.pack()

display_time()
root.mainloop()