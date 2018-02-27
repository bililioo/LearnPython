# -*- coding: utf-8 -*-

# import tkinter
from tkinter import *


# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='hello world')
#         self.helloLabel.pack()
#         self.quitBtn = Button(self, text='quit', command=self.quit)
#         self.quitBtn.pack()

# app = Application()
# app.master.title('hello')
# app.mainloop()

import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameIp = Entry(self)
        self.nameIp.pack()

        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()
        
        self.quitBtn = Button(self, text='exit', command=self.quit)
        self.quitBtn.pack()
    
    def hello(self):
        name = self.nameIp.get() or 'world'
        messagebox.showinfo('message', 'hello %s' % name)

app = Application()
app.master.title('test')
app.mainloop()