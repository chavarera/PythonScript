___________________________

Day 17:Lecture 4
Content:File Methods
Author:Ravishankar Chavare
Date:18-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*File Methods*

*1.flush()*

- *flush()* method is used for flushes the internal buffer.
- While wrting the file operating system store the content of file in the buffer
and buffer content should be write into file using 
1.flush() method 
2.when buffer is full
- python automatically flushes th files when when closing them.
but when we want to flush the data before closing them then the python built in function .*flush()* is used

Syntax:
fileobj.flush()

Example:
#initialize file
fileobj=open("mydata.txt","w")

#Write content to file
fileobj.write("New Content Added")

#flush the Content buffer to file
fileobj.flush()


*2.fileno()*
- fileno returns the integer file desciptor that is used by the implementation to request i/o operation
- file descriptor is simply index into file descriptor table
- for each process in operating system there is one block pcb(process control bloack) 
- one of the part of pcb keep track context of the process which is array structure called file descriptor

Syntax:
fileobj.fileno()

Example:
#initialize file
fileobj=open("mydata.txt","w")

#get file descriptor index value
index_val=fileobj.fileno()
print(index_val)

#Result:3


*3.isatty()*
- *isatty()* return True if a file is connected with terminal device(tty)

Syntax:
fileobj.isatty()

Example:
#initialize file
fileobj=open("mydata.txt","w")

#Check whether file is connected with tty or not
val=fileobj.isatty()
print(val)

#Result:False

*4.seek()*
- set the file cursor current position

Syntax:
 fileobj.seek(position)

Example:
myfile.txt contains
Hi, I am writing simple python programm.

#initilize the file
file=open("myfile.txt","r")

#this will set file reading cursor to 6 th position
position=file.seek(6)

#read content
content=file.read()
print(content)

#Result:am writing simple python programm.

You use 0 as position to set file reading cursor to first position at the starting of file

*5.tell()*
- this method tell the current exact file cursor position in integer

Syntax:
Fileobj.tell()

Example:
myfile.txt contains
Hi, I am writing simple python programm.

#initilize the file
file=open("myfile.txt","r")

#read first 5 characters
data=file.read(5)

#now get the current position of file cursor
pos=file.tell()

#Result:5



*Reading File methods*
*1.read()*
- read the bytes from the file.

*2.readline()*
- read the single line from file

*3.readlines()*
- read all lines in file and return list object.


*Writing File methods*
*1.write()*
- used to write content to the file

*2.writelines()*
- used to write multiple lines to the file list structure is used .
