## User Input

### For Reading User Input
- For reading user input from terminal or shell we used keyword **input()** function.

- In python version 2 we need to get
1. number using **input()** and
2. strings using **raw_input()**

- In python  version 3 **input()**  function handle string as well as number.

Syntax:
```python
input("message")
```
You can put message as blank that is option to show message when accepting user input

Example:
```python
name=input("Enter your name:")
print(name)
#this will accept user input and save it within name variable and print name.
```

You can also ask user message In print statement and later ask user input function using **input()**
```python
username=input('Enter user name:')  #this will ask user on terminal on same line

print('Enter Username:')
uname=input()   #this will ask input on new line

print(username)
print(uname)
```

Note:python 3 consider number and string as data type string while reading from user input

Python 2
```python
nm1=input()
print(type(nm1))
# this will print *int* as data type
```

Python 3
```python
nm1=input()
print(type(nm1))
#this will print *Str* as data type
```

#### Examples
Read string
```python
mystring=input("Enter string")
print(mystring)
```
