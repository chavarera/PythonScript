from tkinter import *
import os
import webbrowser
from tkinter import messagebox as tm
from tkinter import filedialog

def NewFile():
    print('Add code for new file')
def OpenFile():
    name=filedialog.askopenfilename()
    tm.showinfo('File ',os.path.basename(name)+' file Selected ')
    print(name)
def Help():
    webbrowser.open('http://google.com')
def AboutUS():
    tm.showinfo('About Us',' This is simple Demo App\n developed by ravi\n version:0.2')
    
    
root=Tk()
root.title('Simple Menu')
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='New',command=NewFile)
filemenu.add_command(label='Open File',command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

aboutmenu=Menu(menubar,tearoff=0)
aboutmenu.add_command(label='About',command=AboutUS)
aboutmenu.add_command(label='help',command=Help)

menubar.add_cascade(label='Help',menu=aboutmenu)

root.config(menu=menubar)
root.mainloop()
