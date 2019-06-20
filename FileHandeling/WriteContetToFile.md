___________________________

Day 17:Lecture 3
Content: Write content to file
Author:Ravishankar Chavare
Date:18-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________


*Write Contents*

For writing content to a file there are two scenarios

*1.write on existing file.*
- for writing content to a file use following two modes in *open()* function

*Modes for writing file*

1. *"a"*
- This will append the content at the end of file.

2. *"w"*  
- This will overwrite any existing content to a file.

- *write()* function is used to writing the content to a file

Syntax:
fileobj=open(filename,"a/w")
fileobj.write("this is new line ")

Example:
File data.txt contains
Hi,
I am from file

#initialize file
fileobj=open("data.txt","w")

#add new text "I am new text"
fileobj.write("I am new text")

#this will overwrite already content and add new content
Now data.txt contains
I am new text


Example for appending content
Example:
File data.txt contains
Hi,
I am from file

#initialize file
fileobj=open("data.txt","a")

#add new text "I am new text"
fileobj.write("I am new text")

#this will append content 
Now data.txt contains
Hi,
I am from fileI am new text


*2.write on new file after file creating.*

- To create a new file in Python, use the *open()* method, with one of the following parameters:

*"x"*
- Exclusive create
- will create a file, returns an error if the file exist.

*"a" *
- Append mode
- will create a file if the specified file does not exist.

*"w"*
- Write mode
- will create a file if the specified file does not exist.

You can use above modes to create a empty file using *open()* methods

Example:
Consider there is no file named mydata.txt inside current directory.

fil=open("mydata.txt","x")

Here new empty file is created 



*How to write multiline to file*

- The method *writelines()* writes a sequence of strings to the file. 
- The sequence can be any iterable object producing strings, typically a list of strings.

Syntax:
fileobj.writelines(iterable object)


Example:
*mydata.txt* contains
Hi



#initialize file for writing purpose
fil=open("mydata.txt","w")

#lines to write to file
lines=['hello','hi']

#write lines
fil.writelines(lines)

If you check content of file *mydata.txt*
hello
hi

*Write content to file with "with" statement*

Example:
lines=['hello','hi']
with open("mydata.txt","w") as fil:
         fil.writelines(lines)
