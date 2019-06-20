___________________________

Day 17:Lecture 2
Content: Read content of file
Author:Ravishankar Chavare
Date:18-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*1.Read Contents*

- open() method return a file object and file object have a method called *read()* for reading the content of an file.

Syntax:
fillez=open("file name with extenssion","r")
data=filez.read()

Example:
*mylog.txt* contains
Hi, hello i am from python file.

fil=open("mylog.txt","r")
content=fil.read()
print(content)

#Result:Hi, hello i am from python file.


*How to read some content from a file*
- for *read()* method you can pass a integer length of character (number that shows how many characters do you want to read)
- after read statement python cursor will positioned according to given input to *read()* function.

- we can manipulate the python file cursor position using *seek()* function
- *tell()* function is used to getting the current position of cursor in file.

Syntax:
fileobject.read(length)

Example:
*mylog.txt* contains
Hi, hello i am from python file.


Read first 2 character from a mylog.txt file

fil=open("mylog.txt","r")
content=fil.read(2)
print(content)

#Result:Hi

Example 2:
*mylog.txt* contains
Hi, hello i am from python file.

# initialize file for reading purpose
fil=open("mylog.txt","r")

#get cursor position
cur=file.tell()
print(cur)
#Result:0

#Read 2 character from file
fil=open("mylog.txt","r")
content=fil.read(2)
print(content)
#Result:Hi

#Now get updated  cursor position
cur=file.tell()
print(cur)
#Result:2

#Read next 7 character from file
fil=open("mylog.txt","r")
content=fil.read(7)
print(content)
#Result: , hello

#now get the updated cursor position
cur=file.tell()
print(cur)
#Result:9

#now move cursor to 0 position which is start of file
fil.seek(0)




*How to read line from a given file*
- *readline()* function is used to read line from a file.
- By calling *readline()* three times, you can read the three first lines.

Syntax:
fileobject.readlines()

Example:
Consider mydata.txt file contains
First line data 1
Second line data 2
Third line data 3
Fourth line data 4

#read  first line
fil=open("mydata.txt","r")
firstline=fil.readline()
print(firstline)

# Result :First line data 1

*How to read all lines from a file*
- *readlines()* is return list object with every line as element 

Syntax:
fileobj=open(filename,"r")
data=fileobj.readlines()

Example:
mydata.txt contains
First
Second
Third

#initialize file for reading purpose
fil=open("mydata.txt","r")

#read all lines
lines=fil.readlines()
print(lines)

#Result: ['First\n','Second\n','Third']

*Read all file using with statement*

Example:
*mylog.txt* contains
Hi, hello i am from python file.

with open("mylog.txt","r") as fil:
      content=fil.read()
      print(content)

#Result:Hi, hello i am from python file.



*How to use for loop for read all multi line*

fil=open("mydata.txt","r")
for line in fil:
      print(line)

# Result:
First line data 1

Second line data 2

Third line data 3

Fourth line data 4
