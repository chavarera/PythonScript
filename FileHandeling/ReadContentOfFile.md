## Read Content of File :scroll:

### 1.Read Contents :open_file_folder:

- **open()** method return a file object and file object have a method called **read()** for reading the content of an file.

Syntax:
```python
fillez=open("file name with extenssion","r")
data=filez.read()
```


**mylog.txt** contains
```
Hi, hello i am from python file.
```
Example:
```python
fil=open("mylog.txt","r")
content=fil.read()
print(content)

#Result:Hi, hello i am from python file.
```

### How to read some content from a file :scroll:
- for **read()** method you can pass a integer length of character (number that shows how many characters do you want to read)
- after read statement python cursor will positioned according to given input to **read()** function.

- we can manipulate the python file cursor position using **seek()** function
- **tell()** function is used to getting the current position of cursor in file.

Syntax:
```python
fileobject.read(length)
```

**mylog.txt** contains
```
Hi, hello i am from python file.
```
Example:
Read first 2 character from a **mylog.txt** file
```python
#Initialize file for read purpose
fil=open("mylog.txt","r")

#Read 2 byte content of file
content=fil.read(2)

print(content)
#Result:Hi
```


**mylog.txt** contains
```
Hi, hello i am from python file.
```
Example:
```python
# initialize file for reading purpose
fil=open("mylog.txt","r")

#get cursor position
cur=fil.tell()
print(cur)
#Result:0

#Read 2 character from file
fil=open("mylog.txt","r")
content=fil.read(2)
print(content)
#Result:Hi

#Now get updated  cursor position
cur=fil.tell()
print(cur)
#Result:2

#Read next 7 character from file
content=fil.read(7)
print(content)
#Result: , hello

#now get the updated cursor position
cur=fil.tell()
print(cur)
#Result:9

#now move cursor to 0 position which is start of file
fil.seek(0)
```



### How to read line from a given file :open_book:
- **readline()** function is used to read line from a file.
- By calling **readline()** three times, you can read the three first lines.

Syntax:
```python
fileobject.readlines()
```

Consider **mydata.txt** file contains
```
First line data 1
Second line data 2
Third line data 3
Fourth line data 4
```
Example:
```python
#read  first line
fil=open("mydata.txt","r")
firstline=fil.readline()
print(firstline)

# Result :First line data 1
```

### How to read all lines from a file :pencil:
- **readlines()** is return list object with every line as element 

Syntax:
```python
fileobj=open(filename,"r")
data=fileobj.readlines()
```


**mydata.txt** file contains
```
First
Second
Third
```

Example:
```python
#initialize file for reading purpose
fil=open("mydata.txt","r")

#read all lines
lines=fil.readlines()
print(lines)

#Result: ['First\n','Second\n','Third']
```

### Read all file using with statement

File **mylog.txt** contains
```
Hi, hello i am from python file.
```

Example
```python
with open("mylog.txt","r") as fil:
      content=fil.read()
      print(content)

#Result:Hi, hello i am from python file.
```


### How to use for loop for read all multi line :loop:
file **mydata.txt** contains 
```
First line data 1
Second line data 2
Third line data 3
Fourth line data 4
```

Example:
```python
#Initilize file object
fil=open("mydata.txt","r")
for line in fil:
      print(line)

'''
# Result:
First line data 1

Second line data 2

Third line data 3

Fourth line data 4
'''
```
