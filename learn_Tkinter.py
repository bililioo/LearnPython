# -*- coding: utf-8 -*-

# import tkinter
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='hello world')
        self.helloLabel.pack()
        self.quitBtn = Button(self, text='quit', command=self.quit)
        self.quitBtn.pack()

app = Application()
app.master.title('hello')
app.mainloop()