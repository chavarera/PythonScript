## Built In Functions In Regex

### Basic Of Function of Regular Expression

For searching pattern ther are following two ways

**1.single First match**
   - re.search() to find the first match for a pattern.
    
**2.Multiple Match**
  - re.findall() finds all the matches and returns them as a list of strings, with each string representing one match.

#### 1.search

- The **re.search()** method takes a regular expression pattern and a string and searches for that pattern within the string.
- This will return a match object if search is successful Otherwise return None.
- **re.search()** return only first occurence of searching pattern in the input given string.
- add **'r'** before the searching pattern which will be considered as raw string

**group():**
- **group()** is an method for instance of match object.
- Return str or tuple,
- Return subgroup(s) of the match by indices or names

Syntax:
```python
re.search(pattern,string)
```

Example 1:

problem:find out 're' in given string
```python
import re
input_string='this is simple re python program.re is short form of regular expression'
pattern=r're'

search_result=re.search(pattern,input_string)

#Get Type of result
print(type(search_result))

#Result:<class '_sre.SRE_Match'>
#use match object to get the result
if search_result:
    print('Result is found for :'+search_result.group())
else:
    print('Not Found')

'''
#Result
<class '_sre.SRE_Match'>
Result is found for :re
'''
```

#### 2.findall

- findall is used to get the multiple occurences of given patteren.
- The findall() function returns a list containing all matches.
- The list contains the matches in the order they are found.If no matches are found, an empty list is returned.

Syntax:
```
re.findall(pattern,string)
```

Example:
Find out all occurences of 're'
```python
#import Required module
import re

#String
input_string='this is simple re python program.re is short form of regular expression'

#pattern 
pattern='re'

result=re.findall(pattern,input_string)
print(result)

#Result :['re', 're', 're', 're']
```

#### 3.split()
- Returns a list where the string has been split at each match.
- The split() function returns a list where the string has been split at each match.
- If multiple pattern matching in split() function the list is splitted accordingly pattern.
```
input_string:'this is string'
splited list:['th', ' ', ' string']

input_string:'python'
splited list:['p', 'thon']
```

Syntax:
```python
re.split('pattern',input_string)
```

Example:
```python
#import Module
import re

#input String
str = "This is python program"

#Result
result = re.split("python", str)
print(result)

#Result:['This is ', ' program']
```

#### 4.sub()
- Replaces one or many matches with a given input string

consider 
```
input_string :'python'
pattern      : 'py'
replace Text : 'cy'
result of re.sub(): 'cython'
```

Syntax:
```python
re.sub('Search pattern','replace Text',input_string)
```

Example:
```python
#import Module
import re

#input String
input_string = "This is python program"

#replace 'i' with 'it' word in given input_string
result = re.sub('i',"It", input_string)
print(result)

#Result:ThIts Its python program
```
