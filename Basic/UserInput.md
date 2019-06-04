## User :person_with_blond_hair: Input

### For Reading User Input
- For reading user input from terminal or shell we used keyword **input()** function.

- In python version :two: we need to get
1. number using **input()** and
2. strings using **raw_input()**

- In python  version :three: **input()**  function handle string as well as number.

Syntax:
```python
input("message")
```
You can put message  :speech_balloon: as blank that is option to show message when accepting user input :thought_balloon:

Example:
```python
name=input("Enter your name:")
print(name)
#this will accept user input and save it within name variable and print name.
```

You can also ask user message :speech_balloon: In print statement and later ask user input function using **input()**
```python
username=input('Enter user name:')  #this will ask user on terminal on same line

print('Enter Username:')
uname=input()   #this will ask input on new line

print(username)
print(uname)
```

Note:python :three: consider number and string as data type string while reading from user input

Python :two:
```python
nm1=input()
print(type(nm1))
# this will print *int* as data type
```

Python :three:
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
