## String 

### Basic of String
  - The string is a collection of alphabets numbers and special character 
  - Python does not support **char**  datatype. single (length of one ) character also considers as a string.
  - strings are immutable. This means that we can't change any element of a string after the creation of strings. 
  
  ```python
  strings="I am the string"
  #So, we can't do strings[2]='b' as we did with lists
  ```
  - Python strings can be created with single quotes, double quotes, or triple quotes. 
  - When we use triple quotes, strings can span several lines without using the escape character.
  Define string using single quotes  'a'
  ```python
  text1='this is simple string defined using single quotes'
  ```
  
  Define string using double quotes "a"
  ```python
  text1="this is simple string defined using double quotes"
  ```
  Define string using triple quotes '''a'''
  ```python
  text1=''' using triple quotes
  first line
  second line 
  third line
  '''
  ```
you can use here single quotes (') or double quotes (") three times. 

- Unicode in Python
```python
s = "\U00008000"
print(s)
```
Output:
```
耀
```

- You can also define string within braces
```python
mystring=("hello this is the simple string")
print(mystring)
```
Output:
```
hello this is the simple string
```

### Python string escape sequences
- the backslash "\\" is a special character, also called the "escape" character

Example: 
if you want to print It's cold

using escape Character
```python
mystring='It\'s raining'
print(mystring)
```
Output:
```
It's raining
```

we can escape single quotes by just adding double quotes to string 
```python
mystring="It's raining"
print(mystring)
```
Output:
```
It's raining
```


### Accessing String 

- To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring.

```python
var1="Hello I am python learning"

#To print string
print(var1)
```
Output:
```
Hello I am python learning
```

- The string can be accessed using positive and negative indices

#### 1. Positive Indexing 1, 2, 3,
  - Start count indexing from 0,1,2,3,4,5.....
  - first character indexed at 0
  - Last Character indexed at string length-1
    
 Example:
 ```python
 text1='hello this is the simple string'
 
#print first Character
print(text1[0])
#Result:h
 
#print last Character
length=len(text1)
print(text1[length-1])
#Result:g

#print character at 8
print(text1[8])
#Result:i

#if we give index which is not present the error will occur
print(text1[5854584])
#Result: index out of range
 ```
 
 Output:
 ```
h
g
i
Traceback (most recent call last):
  File "/tmp/sessions/b993a699666b4f45/main.py", line 17, in <module>
    print(text1[5854584])
IndexError: string index out of range
 ```
 
 #### 2. Negative Indexing -1 , -2 , -3
- Python supports negative numbers to index a string: -1 means the last char, -2 is the next to last, and so on. 
- In other words -1 is the same as the index len(s)-1, -2 is the same as len(s)-2.
Example:
 ```python
 text1='hello this is the simple string'
 
#print first Character
length=len(text1)
print(text1[-length])
#Result:h

#print last Character
print(text1[-1])
#Result:g

#print character at -8
print(text1[-8])
#Result:e

#if we give index which is not present the error will occur
print(text1[-4584])
#Result: index out of range
 ```
Output:
```
h
g
e
Traceback (most recent call last):
  File "/tmp/sessions/216f0490751a0a75/main.py", line 17, in <module>
    print(text1[-4584])
IndexError: string index out of range
```
 
 ### Accessing multiple Characters(substring)  from string
 - we can access substring using slicing ([:])
 
 Syntax:
 ```python
 stringname[start_index:end_index]
 ```
  
 1. **start_index**: will be considered the string starting point which is included in the result
 2. **end_index**: will be consider ending point of string which be excluded from the result
 
 Example Using Positive Index
 ```python
 text1='hello python'

#to print 'hel' from above string we need to slice using
start=0
#here text[0]:h,text1[1]:e,text1[2]:l,text1[3]:l....
end=3 
substring=text1[start:end]

# start can be blank if you are extracting the string from starting index
substring1=text1[:end]
print("text1[:end]:-", substring)

#to print 'hon' from above string we need to slice using
start=-3
end=-1 #here text[-1]:n,text1[-2]:o,text1[-3]:h....
substring=text1[start:end]
# end can blank if you are extracing string till last charcater index
substring1=text1[start:]
print("text1[start:]:-",substring)
#Result:hon

#to print 'pyt' from above string
substring=text1[6:9] 
print("text1[6:9]:-",substring)
#Result:pyt

#if you give out of range index while slicing it doesn't give any error
substring=text1[5458:] 
print("text1[5458:]:-",substring)
#Result:''

substring1=text1[:5458] 
print("text1[:5458]:-",substring1)
#Result:'hello python'
 ```
Output:
```
text1[:end]:- hel
text1[start:]:- ho
text1[6:9]:- pyt
text1[5458:]:- 
text1[:5458]:- hello python
```
 
Example Using Negative Index 
```python
text1='hello python'

#to print 'hon' from the above string we need to slice using
substring=text1[-3:]
print(substring)

#to print 'pyt' from above string
substring=text1[-6:-3] 
#Result:pyt

#if you give out of range index while slicing it doesn't give any error
substring=text1[-5458:]
print(substring)
#Result:'hello python'

substring1=text1[:-458] 
print(substring)
#Result:''
```
Output:
```
hon
hello python
hello python
```
 
