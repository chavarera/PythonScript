## String :abcd:

### Basic of String
  - String is collection of Alphabets :a: numbers and special character :congratulations:.
  - Python does not support **char**  datatype. single (length of one ) :a: character also consider as string.
  - strings are immutable. This means that we that we can't :no_entry_sign: change any element of a string after creation of strings. 
  
  ```python
  strings="I am string"
  #So, we can't do strings[2]='b' as we did with lists
  ```
  - Python strings can be created with single quotes , double quotes , or triple quotes . 
  - When we use triple quotes, strings can span several lines without using the escape character.
  Define string using single quotes  ':a:'
  ```python
  text1='this is simple string defined using single quotes'
  ```
  
  Define string using double quotes ":a:"
  ```python
  text1="this is simple string defined using double quotes"
  ```
  Define string using triple quotes ''':a:'''
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

#result:'耀'
```
- You can also define string within braces
```python
mystring=("hello this is simple string")
print(mystring)

#result:'hello this is simple string'
```

### Python string escape sequences
- the backslash "\\" is a special character, also called the "escape" character

Example : if you want to print It's cold

using escape Character
```python
mystring='It\'s raining'
print(mystring)

#result:"It's raining"
```

we can escape single quotes by just adding double quotes to string 
```python
mystring="It's raining"
print(mystring)

#result:"It's raining"
```


### Accessing String :capital_abcd:

- To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring.

```python
var1="Hello I am python learning"
#To print string
print(var1)

#Result:Hello I am python learning
```


- String can be accesssed using positive and negative indices

#### 1. Positive Indexing :one: :two: :three: :
  - Start count indexing from 0,1,2,3,4,5.....
  - first character indexed at 0
  - Last Character indexed at string length-1
    
 Example:
 ```python
 text1='hello this is simple string'
 
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

#if we give index which is not present the error will occure
print(text1[5854584])
#Result:index out of range

 ```
 #### 2. Negative Indexing -:one: -:two: -:three::
- Python supports using negative numbers to index into a string: -1 means the last char, -2 is the next to last, and so on. 
- In other words -1 is the same as the index len(s)-1, -2 is the same as len(s)-2.
Example:
 ```python
 text1='hello this is simple string'
 
 #print first Character
 length=len(text1)
 print(text1[-length])
 #result:h
 
 #print last Character
 print(text1[-1])
 #result:g

#print character at -8
print(text1[-8])
#result:e

#if we give index which is not present the error will occure
print(text1[-4584])
#result:index out of range
 ```
 
 ### Accessing multiple Characters(substring) :abc: from string
 - we can access substring using slicing ([:])
 
 Syntax:
 ```python
 stringname[startindex:endindex]

 ```
  
 1. startindex: will be consider the string statring point which be included in result
 2. endindex: will be consider ending point of string which be excluded from result
 
 Example Using Positive Index :ab: :
 ```python
 text1='hello python'
 
 #to print 'hel' from above string we need to slice using
 start=0
 #here text[0]:h,text1[1]:e,text1[2]:l,text1[3]:l....
 end=3 
 substring=text1[start:end]
 
 # start can be blank if you are extracing string from starting index
 substring1=text1[:end]
 print(substring)
 
 #to print 'hon' from above string we need to slice using
 start=-3
 end=-1 #here text[-1]:n,text1[-2]:o,text1[-3]:h....
 substring=text1[start:end]
 # end can blank if you are extracing string till last charcater index
 substring1=text1[start:]
 print(substring)
 
 #to print 'pyt' from above string
 substring=text1[6:9] 
 #result:pyt
 
 #if you give out of range index while slicing it doesn't give any error
 substring=text1[5458:] #result:''
 substring1=text1[:5458] #result:'hello python'
 ```
 
Example Using Negative Index :recycle: :
```python
 text1='hello python'

 #to print 'hon' from above string we need to slice using
 substring=text1[-3:]
 print(substring)
 
 #to print 'pyt' from above string
 substring=text1[-6:-3] #
 result:pyt
 
 #if you give out of range index while slicing it doesn't give any error
 substring=text1[-5458:] #result:'hello python'
 substring1=text1[:-458] #result:''

```

 
