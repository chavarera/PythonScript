## Read Content of File 

### 1.Read Contents 

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
```
Output:
```
Hi, hello i am from python file.
```

### How to read some content from a file
- for **read()** method you can pass an integer length of character (a number that shows how many characters do you want to read)
- after reading statement python cursor will position according to given input to **read()** function.

- we can manipulate the python file cursor position using **seek()** function
- **tell()** function is used to getting the current position of the cursor in file.

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
Output:
```
Hi
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
print("Current Position of Cursor")
print(cur)
#Result:0

#Read 2 character from file
fil=open("mylog.txt","r")
content=fil.read(2)
print("\nRead 2 character from file")
print(content)
#Result:Hi

#Now get updated  cursor position
cur=fil.tell()
print("\nupdated  cursor position")
print(cur)
#Result:2

#Read next 7 character from file
content=fil.read(7)
print("\nRead next 7 character from file")
print(content)
#Result: , hello

#now get the updated cursor position
cur=fil.tell()
print("\nupdated cursor position")
print(cur)
#Result:9

#now move cursor to 0 position which is start of file
print("\nnow move cursor to 0 position which is start of file")
fil.seek(0)

#Print Current Cursor  Position
print("\n Current Cursor Position")
print(fil.tell())
```

Output:
```
Current Position of Cursor
0

Read 2 character from file
Hi

updated  cursor position
2

Read next 7 character from file
, hello

updated cursor position
9

now move cursor to 0 position which is start of file

 Current Cursor Position
0
```



### How to read a line from a given file 
- **readline()** function is used to read a line from a file.
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
#Create File Object For Reading Purpose
fil=open("mydata.txt","r")

#Read First File From File
firstline=fil.readline()

#Print First File
print(firstline)
```
Output:
```
First line data 1
```

### How to read all lines from a file
- **readlines()** is return list object with every line as an element 

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

#read all lines and Store it in list
lines=fil.readlines()

#Print All Lines List
print(lines)
```

Output:
```
['First\n', 'Second\n', 'Third']
```

### Read all file using  "with"  statement

File **mylog.txt** contains
```
Hi, hello i am from python file.
```

Example
```python
#Read File using  with loop
with open("mylog.txt","r") as fil:
  content=fil.read()
  print(content)
```
Output:
```
Hi, hello i am from python file.
```


### How to use for loop for reading all multi-line
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

#Use for loop Print line by line 
for line in fil:
  print(line)
```
Output:
```
First line data 1

Second line data 2

Third line data 3

Fourth line data 4
```
