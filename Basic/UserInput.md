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
#when user input 5 as nm1
print(type(nm1))
# this will print *int* as data type
```

Python :three:
```python
nm1=input()
#when user input 5 as nm1
print(type(nm1))
#this will print *Str* as data type
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
**end**: end is printed at last
**file**:  must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
**flush**: If True, the stream is forcibly flushed. Default value: False.

Example:
Normaal single object print
```python
mystring="i am python"
number=5

#print mystring and number
print(mystring)
print(number)

#Result:i am python
#Result:5
```

Pass Multiple Objects to print()
```python
mystring="i am python"
number=5

#print mystring and number
print(mystring,number)

#Result:i am python 5

```
#### Using Seperator
syntax:
```python
print(element, sep='seperator')
```

Example:
```python
a=5
print(a, sep='--')

#Result:--5
```

