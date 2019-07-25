## Identifiers

You can use different identifiers with modifiers to achieve different pattern searching.

### 1.Numbers

**\d** Any Number

**\D** Anything except Number

- matches number 0,1,2,3,4,5,6,7,8,9

Syntax:
```python
pattern='\d'
```

Example:
```python
import re
input_string='today date is 21 feb 2019'

#Read Numbers
pattern=r'\d'
result=re.findall(pattern,input_string)
print(result)
#Result:['2', '1', '2', '0', '1', '9']


#Find Numbers in groupusing + modifiers
pattern=r'\d+'
result=re.findall(pattern,input_string)
print(result)
#Result:['21', '2019']


#Find out 2 digit number
pattern=r'\d{2}'
result=re.findall(pattern,input_string)
print(result)
#Result:['21', '20', '19']

#Find out all text without number
pattern=r'\D'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:
['t', 'o', 'd', 'a', 'y', ' ', 'd', 'a', 't',
'e', ' ', 'i', 's', ' ', ' ', 'f', 'e', 'b', ' ']
'''


#Find a any number followed by 2 and number should be 3 digit
pattern=r'2[\d]{2}'
result=re.findall(pattern,input_string)
print(result)
#Result:['201']


#Find Numbers in groupusing * modifiers
pattern=r'\d*'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:
['', '', '', '', '', '', '', '', '', '', '',
'', '', '', '21', '', '', '', '', '', '2019', '']
'''
```


### 2.Strings

**\w** matches with alphabets and numbers only

   a,b,c...z   A,B,C.....Z,0,1,2,3,4,5,6,7,8,9

**\W** anything without a string

Example:
```python
import re

input_string='Hi @ gmail 12'

#Find normal string characters
pattern=r'\w'
result=re.findall(pattern,input_string)
print(result)
#Result:['H', 'i', 'g', 'm', 'a', 'i', 'l', '1', '2']



#Find normal string characters with grouping modifiers
pattern=r'\w+'
result=re.findall(pattern,input_string)
print(result)
#Result:['Hi', 'gmail', '12']


#Findout 2 length character string
pattern=r'\w{2}'
result=re.findall(pattern,input_string)
print(result)
#Result:['Hi', 'gmail', '12']


#Check input string starting with Hi
pattern=r'^Hi'
result=re.findall(pattern,input_string)
print(result)
#Result:['Hi']
```


### 3.Anything (but not newline character)
**.**
- .(dot) is used to achieve create pattern that result any character but except new line.
- This will match anything but not a new line

Example:
```python
import re

input_string='This is simple example, \n contains three lines \n @$# 4555'

#using + modifiers This doesn't match new line character that is /n
pattern=r'.+'
result=re.findall(pattern,input_string)
print(result)
#Result:['This is simple example, ', ' contains three lines ', ' @$# 4555']
```

### 4.Space
**\s** space

**\S** anything Except Space

- matches A whitespace character 

 A whitespace character can be:

- A space character
    - A tab character
    - A carriage return character
    - A new line character
    - A vertical tab character
    - A form feed character

Example:
```python
import re

input_string='This is simple example'

#get no of spaces in input string
pattern=r'\s'
result=re.findall(pattern,input_string)
print(result)
#Result: [' ', ' ', ' ']

#return all text except space characters
pattern=r'\S+'
result=re.findall(pattern,input_string)
print(result)
#Result: ['This', 'is', 'simple', 'example']

```
