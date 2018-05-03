from tkinter import *
import os   #os module to perform os related operation like os.path.basename(fullpath)
import webbrowser   #webbrowser module to open the given webpage
from tkinter import messagebox as tm    #messagebox module for showing msg
from tkinter import filedialog  #filedialog to select the file from local system


#function NewFile when user click on New Option Under File menu this will called
def NewFile():
    print('Add code for new file')

#function OpenFile when user click on Open Option Under File menu this will called
def OpenFile():
    name=filedialog.askopenfilename()
    tm.showinfo('File ',os.path.basename(name)+' file Selected ')
    print(name)

#function for help when user select help
def Help():
    webbrowser.open('http://google.com')

#this function show messagebox dialog to user about developer
def AboutUS():
    tm.showinfo('About Us',' This is simple Demo App\n developed by ravi\n version:0.2')
    
    
root=Tk()
#simple window title
root.title('Simple Menu')

#define menubar first
menubar=Menu(root)

#now create filemenu
filemenu=Menu(menubar,tearoff=0)

#menu option under File 
filemenu.add_command(label='New',command=NewFile)
filemenu.add_command(label='Open File',command=OpenFile)

#used for giving seperator between two elemnt of menu
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

#now add file menu to menubar
menubar.add_cascade(label='File',menu=filemenu)



#now create about menu
aboutmenu=Menu(menubar,tearoff=0)

#add options to about menu
aboutmenu.add_command(label='About',command=AboutUS)
aboutmenu.add_command(label='help',command=Help)

#add about menu to menubar
menubar.add_cascade(label='Help',menu=aboutmenu)

#now finally configure menu with menubar
root.config(menu=menubar)
root.mainloop()
