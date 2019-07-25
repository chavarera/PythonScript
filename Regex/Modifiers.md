## Modifiers in Regular Expression


#### Modifiers Examples

- **\w** is an one Identifier used to to search a string pattern .
- **\d** is an one Identifier used to to search a numerical pattern .

### 1.+ Match 1 or More

- Match 1 or More
- **+** will match the pattern untill it will get success result means till pattern match

Examples:
```python
#import require module
import re

#input string for Number
input_string='today date is 19 jan 2019'

#Find Number without Modifiers
pattern=r'\d'
result=re.findall(pattern,input_string)
print(result)
#Result:['1', '9', '2', '0', '1', '9']

#Find number Using + modifiers
pattern1=r'\d+'
result=re.findall(pattern1,input_string)
print(result)
#Result:['19', '2019']


#Find string without modifiers
pattern=r'\w'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:['t', 'o', 'd', 'a', 'y', 'd', 'a', 't', 
'e', 'i', 's', '1', '9', 'j', 'a', 'n', '2', '0', '1', '9']
'''


#Find using Using + modifiers
pattern1=r'\w+'
result=re.findall(pattern1,input_string)
print(result)
#Result:['today', 'date', 'is', '19', 'jan', '2019']
```



### 2. * Match 0 or more 

- Match 0 or more
- If match not found blank is returned.
- Even space is considered as match.

Example:
```python
#import require module
import re

#input string for Number
input_string='today date is 19 jan 2019'

#Find Number without Modifiers
pattern=r'\d'
result=re.findall(pattern,input_string)
print(result)
#Result:['1', '9', '2', '0', '1', '9']

#Find number Using * modifiers
pattern1=r'\d*'
result=re.findall(pattern1,input_string)
print(result)
'''
#Result:['', '', '', '', '', '', '', 
'', '', '', '', '', '', '', '19', '', '', '', '', '', '2019', '']
'''

#Find string without modifiers
pattern=r'\w'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:['t', 'o', 'd', 'a', 'y', 'd', 'a', 't', 
'e', 'i', 's', '1', '9', 'j', 'a', 'n', '2', '0', '1', '9']
'''


#Find using Using * modifiers
pattern1=r'\w*'
result=re.findall(pattern1,input_string)
print(result)
#Result:['today', '', 'date', '', 'is', '', '19', '', 'jan', '', '2019', '']
```




### 3.? Match 0 or 1
- Match 0 or 1

Example:
```python
#import require module
import re

#input string for Number
input_string='today date is 19 jan 2019'

#Find Number without Modifiers
pattern=r'\d'
result=re.findall(pattern,input_string)
print(result)
#Result:['1', '9', '2', '0', '1', '9']

#Find number Using ? modifiers
pattern1=r'\d?'
result=re.findall(pattern1,input_string)
print(result)
'''
#Result:'', '', '', '', '', '', '', '', '', 
'', '', '', '', '', '1', '9', '', '', '', '', '', '2', '0', '1', '9', '']
'''

#Find string without modifiers
pattern=r'\w'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:['t', 'o', 'd', 'a', 'y', 'd', 'a', 't', 
'e', 'i', 's', '1', '9', 'j', 'a', 'n', '2', '0', '1', '9']
'''


#Find using Using ? modifiers
pattern1=r'\w?'
result=re.findall(pattern1,input_string)
print(result)
'''
#Result:
['t', 'o', 'd', 'a', 'y', '', 'd', 'a', 't', 'e', '', 'i', 's',
'', '1', '9', '', 'j', 'a', 'n', '', '2', '0', '1', '9', '']

'''
```



### 4.{} expecting result count

- Describing about numbers expecting result

Syntax:
```python
{x}	# Display x number of result
{x,y}	# Display result count should be between x or y
```
Example:
```python
using {Number}
#import require module
import re

#input string for Number
input_string='today date is 19 jan 2019'

#Get 1 Digit Number
pattern=r'\d{1}'
result=re.findall(pattern,input_string)
print(result)
#Result:['1', '9', '2', '0', '1', '9']

#Get 2 Digit Number
pattern=r'\d{2}'
result=re.findall(pattern,input_string)
print(result)
#Result:['19', '20', '19']


#Get 3 Digit Number
pattern=r'\d{3}'
result=re.findall(pattern,input_string)
print(result)
#Result:['201']


#Get 3 Character string from input string
pattern=r'\w{3}'
result=re.findall(pattern,input_string)
print(result)
#Result:['tod', 'dat', 'jan', '201']

#Get 5 Character string from input string
pattern=r'\w{5}'
result=re.findall(pattern,input_string)
print(result)
#Result:['today']
```

Example 2:
Using {start,end}
```
#import require module
import re

#input string for Number
input_string='today date is 19 jan 2019'

#1 to 2 digit number
pattern=r'\d{1,2}'
result=re.findall(pattern,input_string)
print(result)
#Result:['19', '20', '19']


#frequency of matched between 2 to 4 charachater
pattern=r'\w{2,4}'
result=re.findall(pattern,input_string)
print(result)
#Result:['toda', 'date', 'is', '19', 'jan', '2019']
```
 
### 5.^ begining of string

- matching the beginning of the string.
- The caret ^ matches at the beginning of the given input text.

Syntax:
```python
pattern=r'^searching pattern'
```
Example:
```python
import re
input_string='Python is programming language'

#check whether given input start with Python
pattern='^Python'
result=re.findall(pattern,input_string)
print(result)
#Result:['Python']

input_string2='Programming language is Python'
result2=re.findall(r'^Python',input_string2)
print(result2)
#Result:[]
```

### 6.$ end of the string

- Matching the end of the string.
- The caret ^ matches at the ending of the given input text.

Syntax:
```python
pattern=r'$searching pattern'
```

Example:
```python
import re
input_string='Python is programming language'


#check whether given input start with Python
pattern='Python$'
result=re.findall(pattern,input_string)
print(result)
#Result:[]
#Here Given text not ends with 'Python' hence it will return a blank  list

#Here given text is end with 'Python'
input_string2='Programming language is Python'
result2=re.findall(r'Python$',input_string2)
print(result2)
#Result:['Python']
```

### 7.| or
- Either or Example({1}|{3})
- In or statement if the first pattern is matched then second pattern in or will ignores.
- If first pattern is not matched then second pattern is checked

Consider
```
input_string :'20 jan 2019 . 142'
pattern1     :r'(\d{4}|\d{2})'
result1      :['20', '2019', '14']

pattern2     :r'(\d{2}|\d{4})'
result2      :['20', '20', '19', '14']
```

Syntax:
```python
pattern='some_pattern | another pattern'
```

Example:
```python
import re
input_string='20 jan 2019 . 142'

#Search a number either 2 digit or 4 digit
pattern=r'(\d{4}|\d{2})'
result=re.findall(pattern,input_string)
print(result)

#Result:['20', '2019', '14']
```

### 8.[] raning modifiers

- range or variance

Syntax:
```
[....]
    - Any one of the characters.
    - [abc] matches 'a','b','c'
    - [0123] matches '0','1','2','3'

[.-.]
    - Range expression.
    - any one of the characters in the input range.
    - [0-4] matches 0,1,2,3,4
    - [A-Z] matches camel case alphabets A,B,C,D,E......Z
    - [a-z] matches small letter alphabets a,b,c,d,e,f...z

[^...]
    - Not one of the characters.
    - [^0-9]  matches any non-digit.

```

Example:
```python
import re
input_string='i am Learning python from 10 days 7589462'

#findout any characters from a,e,i,o,u
pattern=r'[aeiou]'
result=re.findall(pattern,input_string)
print(result)
#Result:['i', 'a', 'e', 'a', 'i', 'o', 'o', 'a']

#findout Numbers ranging from 0-5
pattern=r'[0-5]'
result=re.findall(pattern,input_string)
print(result)
#Result:['1', '0', '5', '4', '2']


#findout any character ranging a-f
pattern=r'[a-f]'
result=re.findall(pattern,input_string)
print(result)
#Result:['a', 'e', 'a', 'f', 'd', 'a']

#findout non digit characters
pattern=r'[^0-9]'
result=re.findall(pattern,input_string)
print(result)
'''
#Result:
['i', ' ', 'a', 'm', ' ', 'L', 'e', 'a', 'r', 'n', 'i',
'n', 'g', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'f',
'r', 'o', 'm', ' ', ' ', 'd', 'a', 'y', 's', ' ']

'''
```
