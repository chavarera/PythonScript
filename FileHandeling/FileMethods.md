## File Methods

### File Methods

### 1.flush()

- **flush()** method is used for flushes the internal buffer.
- While writing the file operating system store the content of the file in the buffer
and buffer content should be written into a file using 
   - flush() method 
   - when the buffer is full
- python automatically flushes the files when closing them.
but when we want to flush the data before closing them then the python built-in function .*flush()* is used

Syntax:
```python
fileobj.flush()
```
Example:
```python
#initialize file
fileobj=open("mydata.txt","w")

#Write content to file
fileobj.write("New Content Added")

#flush the Content buffer to file
fileobj.flush()
```

### 2.fileno()
- fileno returns the integer file descriptor that is used by the implementation to request i/o operation
- the file descriptor is simply indexed into a file descriptor table
- for each process in the operating system, there is one block PCB(process control block) 
- one of the parts of PCB keep track context of the process which is array structure called file descriptor

Syntax:
```python
fileobj.fileno()
```

Example:
```python
#initialize file
fileobj=open("mydata.txt","w")

#get file descriptor index value
index_val=fileobj.fileno()
print(index_val)
```
Output:
```
3
```

### 3.isatty()
- **isatty()** return True if a file is connected with terminal device(tty)

Syntax:
```python
fileobj.isatty()
```

Example:
```python
#initialize file
fileobj=open("mydata.txt","w")

#Check whether file is connected with tty or not
val=fileobj.isatty()
print(val)
```
Output:
```
False
```


### 4.seek()
- set the file cursor current position

Syntax:
```python
 fileobj.seek(position)
```
File **myfile.txt** contains
```
Hi, I am writing simple python programm.
```

Example:
```python
#initilize the file
file=open("myfile.txt","r")

#this will set file reading cursor to 6 th position
position=file.seek(6)

#read content
content=file.read()
print(content)
```
Output:
```
am writing simple python programm.
```

You use 0 as a position to set file reading cursor to the first position at the starting of file

### 5.tell()
- this method tell the current exact file cursor position in integer

Syntax:
```python
Fileobj.tell()
```

File **myfile.txt** contains
```
Hi, I am writing simple python programm.
```

Example:
```python
#initilize the file
file=open("myfile.txt","r")

#read first 5 characters
data=file.read(5)

#now get the current position of file cursor
pos=file.tell()
```
Output:
```
5
```



## Reading File methods
**1.read()**
- read the bytes from the file.

**2.readline()**
- read the single line from file

**3.readlines()**
- read all lines in file and return list object.


## Writing File methods
**1.write()**
- used to write content to the file

**2.writelines()**
- used to write multiple lines to the file list structure is used.
