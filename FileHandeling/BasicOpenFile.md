## File Handling
### Basic Of  File
- A file is some information or data which stays in the computer storage devices.
- Generally, we divide files into two categories, text file, and binary file. 
**Text** files are the simple text whereas the **binary** files contain binary data which is only readable by a computer

- Python has several functions for creating, reading, updating, and deleting files.

There are mainly different 3 operations can be performed on the file.
 - Open file
 - Read or write file
 - close file.

### 1.Opening File
- for opening a file in Python one named **open()** methods are available.

- The open function takes two arguments
  - filename
  - mode of file


Syntax:
```python
File_to_open=open(filename,mode)
```
Where 
Filename; required
Mode:is optional bydefault mode is **read**

### Following are some modes which are helpful while dealing with file

#### 1. r 
- Read mode
- This mode opens a file for reading purposes.
- If the file does not exist this will generate an error.

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
- This mode is used when we want to append content to the end of the file without overwintering the previous content.
- If the file does not exist *a* mode creates a new file.

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
- If the file does not exist it will create a new file.

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
- If the file already exists then it will give an error

Syntax:
```python
fileobj=open(filename,"x")
```

Example:
```python
fileobj=open("myfile.txt","x")
```

the file should be handled as binary or text mode using the following 2 modes

1. **b** binary file
2. **t** text file


Example 1:

Consider **mylog.txt** file in your current directory and you want to open it
```python
#defualt read mode
fil=open("mylog.txt")

#Using r mode
fil=open("mylog.txt","r")

#using read and text mode
fil=open("mylog.txt","rt")
```

Above all example open a text file for reading the purpose


Example 2:

Open file for writing purpose
```python
fil=open("mylog.txt","w")
```

### How to add multiple modes to file object

When you want to read and write on the same file you can pass both modes to open() function

Syntax:
```python
fileobj=open(filename,"mode1mode2")
```
Example:
```python
fileobj=open("myfile.txt","rwt")
```
Here file is opened in three different mode for reading,writing a text file

**Note**:after completion of file operation don't forgot to close file using 
filename.close()

### Open a file with "with" statement

- With the **with** statement, you get better syntax and exceptions handling.
- Using with keyword the file is automatically closed when the operation is completed.we don't need to write 
```python
fileobj.close()
```
Syntax:
```python
with open(filename,mode) as fileobj:
         #do operation on fileobj
```

Example:

Consider **mytext.txt** contains
```
Hello I am from file
```
```python
with open("mytext.txt","r") as file:
    content=file.read()
    print(content)
```
Output:
```
Hello I am from file
```
