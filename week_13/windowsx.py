#!/usr/bin/python3
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.varSausage = BooleanVar()
        self.varPepp = BooleanVar()
        self.create_widgets()
        
    def create_widgets(self):
        self.label1 = Label (self, text='What do you want on your Pizza?')
        self.label1.grid(row=0, column=0, sticky=W)
        
        self.check1 = Checkbutton (self, text='Sausage', variable=self.varSausage)
        self.check1.grid(row=1, sticky=W)
        
        self.check2 = Checkbutton (self, text='Pepperoni', variable=self.varPepp)
        self.check2.grid(row=2, sticky=W)
        
        self.button1 = Button (self, text='Order', command=self.display)
        self.button1.grid(row=3)
        
    def display(self):
        if (self.varSausage.get()):
            print('You want sausage')
        if (self.varPepp.get()):
            print('You want pepperoni')
        if (not self.varSausage.get() and not self.varPepp.get()):
            print('You do not want anything on your pizza')
        print('______________________________')
        
root = Tk()
root.title('Test check button')
root.geometry('500x100')
app = Application(root)
app.mainloop()
