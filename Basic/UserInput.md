## User  Input

### For Reading User Input
- For reading user input from terminal or shell we used keyword **input()** function.

- In python version 2 we need to get
1. number using **input()** and
2. strings using **raw_input()**

- In python version 3 **input()**  function handle string as well as number.

Syntax:
```python
msg=input("message")
print(msg)
```
You can put message  as a blank that is an option to show message when accepting user input

Example:
```python
name=input("Enter your name:")
print(name)
#this will accept user input and save it within 
#name variable and print name.
```

You can also ask user message  In a print statement and later ask user input function using **input()**
```python
#this will ask user on terminal on same line
username=input('Enter user name:')  

print('Enter Username:')
uname=input()   #this will ask input on new line

print(username)
print(uname)
```

Note: python 3 consider number and string as data type string while reading from user input

Python 2
```python
nm1=input()
#when user input 5 as nm1
print(type(nm1))
# this will print *int* as data type
```
Output
```
5
<class 'int'>
```

Python 3
```python
nm1=input()
#when user input 5 as nm1
print(type(nm1))
#this will print *Str* as data type
```
Output
```
5
<class 'str'>
```

#### Examples
Read string
```python
mystring=input("Enter string")
print(mystring)
```
### For Printing Output on Console
- The **print()** function prints the given object to the standard output device (screen) or to the text stream file.

Syntax:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
**objects**: object to the printed. * indicates that there may be more than one object

**sep**: objects are separated by sep. Default value: ' '

**end**: the end is printed at last

**file**:  must be an object with a write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.

**flush**: If True, the stream is forcibly flushed. Default value: False.

Example:
Normal single object print
```python
#intilize The Variable
mystring="i am python"
number=5

#print mystring and number
print(mystring)
print(number)
```

Output
```
i am python
5
```

Pass Multiple Objects to print()
```python
#Assign Variable and numbers
mystring="i am python"
number=5

#print mystring and number
print(mystring,number)
```

Output
```
i am python 5
```
