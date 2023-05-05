#!/usr/bin/python3

from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.pack()
        
root = Tk()
root.title('This is a test window')
root.geometry('800x400')
app = Application(root)
app.mainloop()