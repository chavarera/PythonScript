## File Handeling
### File
- A file is some information or data which stays in the computer storage devices.
-Generally we divide files in two categories, text file and binary file. 
**Text** files are simple text where as the *binary* files contain binary data which is only readable by computer

- Python has several functions for creating, reading, updating, and deleting files.

There are mainly different 3 operation can be performed on file.
 1.Open file
 2.Read or write file
 3.close file.

### 1.Opening File
- for opening a file in Python one named *open()* methods is available.

- The open function takes two arguments
  1.filename
  2.mode of file


Syntax:
```python
File_to_open=open(filename,mode)
```
Where 
Filename; required
Mode:is optional bydefault mode is **read**

### Following are the some modes which are helpful while dealing with file

#### 1. r 
- Read mode
- This mode open a file for reading purpose.
- If file is not exists this will generate error.

Syntax:
```python
fileobj=open(filename,"r")
```
Example:
```python
fileobj=open("myfile.txt","r")
```
Above example give an error if file is not exists.


### 2. a 
- Append mode
- This mode is used when we want to append content to end of file without overwintering the previous content.
- If file is not exists *a* mode create a new file.

Syntax:
```python
fileobj=open(filename,"a")
```
Example:
```python
fileobj=open("myfile.txt","a")
```

### 3. w
- Write mode 
- This mode is used when we want to overwrite some content to file.
- If file is not exists it will create new file.

Syntax:
```python
fileobj=open(filename,"w")
```

Example:
```python
fileobj=open("myfile.txt","w")
```

### 4. x 
- Exclusive Create.
- This mode is used to create a specified file.
- If file is already exists then it will give an error

Syntax:
fileobj=open(filename,"x")


Example:
fileobj=open("myfile.txt","x")


the file should be handled as binary or text mode using following 2 modes

*b* binary file
*t* text fil


Example 1:
Consider *mylog.txt* file in your current directory and you want to open it

#defualt read mode
fil=open("mylog.txt")

#Using r mode
fil=open("mylog.txt","r")

#using read and text mode
fil=open("mylog.txt","rt")

Above all example open text file for reading purpose


Example 2:
Open file for writing purpose

fil=open("mylog.txt","w")

*How to add multiple mode to fileobject*

When you want to read and write on same file you can pass both mode to open() function

Syntax:
fileobj=open(filename,"mode1mode2")

Example:
fileobj=open("myfile.txt","rwt")

Here file is opened in three different mode for reading,writing a text file

*Note*:after completion of file operation don't forgot to close file using 
filename.close()

*Open a file with "with" statement*

- With the "With" statement, you get better syntax and exceptions handling.
- Using with keyword the file is automatically closed when operation are completed.we don't need to write 
fileobj.close()

Syntax:
with open(filename,mode) as fileobj:
         #do operation on fileobj


Example:
Consider *mytext.txt* contains
Hello I am from file

with open("mytext.txt","r") as file:
          content=file.read()
          print(content)

#Result :Hello I am from file
