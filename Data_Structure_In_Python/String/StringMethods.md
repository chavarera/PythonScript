## String  Methods

- Python  has a set of built-in methods that you can use on strings
- All string methods return new values.they do not change the original string because the string is an immutable python object.

Following are the most commonly used method for strings are

## 1. capitalize():
- The **capitalize()** method upper case the first letter in the given sequences(string).

Example:
```python
text="hello"
result=text.capitalize()
print(result)
```
Output:
```
Hello
```

## 2. count():
- The **count()** method returns the number of times a specified value appears in the string.
- Returns the frequency of given element inside string.
Syntax:
```python
string.count("Value")
```

Example:
```python
text1="Hello"
result=text1.count('l')
result1=text1.count('H')

print(result) 
#Result:2

print(result1) 
#Result:1
```

Output:
```
1
```
Search Element Count From Some SPecific Index

Syntax:
```python
string.count(value, start, end)
```

1. **value**:-    element which does you want to find count.
2. **start**:-    Default is 0, starting position of an element.
3. **end**:-      Default is len(string) ,ending position of an element.

For Example
```python
text1="This is simple Text"
result=text1.count('i')
res=text1.count('i',6,len(text1))
print(result) 
#Result:3

print(res) 
#Result :1
```

Output:
```
3
1
```

## 3. endswith():

- The **endswith()** method returns True if the string ends with the specified value, otherwise False.

Example:
```python
text1="This is simple Text."
result=text1.endswith('.')
print(result)
#Result:True
````
Output:
```
True
```

## 4. index() :
- The **index()** method finds the first occurrence of the specified value.
- The **index()** method raises an exception if the value is not found.

Example:
```python
mystring="I am python"
print(mystring.index('a')) 
#Result:2

print(mystring.index('k')) 
#Result:error:-substring not found

```

Output:
```
2
Traceback (most recent call last):
  File "/tmp/sessions/7f5718dc77646b8f/main.py", line 5, in <module>
    print(mystring.index('k')) 
ValueError: substring not found
```


## 5. find():
- To find out position of word or character from given string or paragraph use **find()** method.
- The **find()** method finds the first occurrence of the specified value.
- The **find()** method returns -1 if the value is not found.

Syntax
```python
string.find(str, startpoint, endpoint)
```
**str**:-which string to find
**startpoint**:-the starting  index from where you want to find a string
**endpoint**:-Ending index

Example 1:

```python
text="Python"
result=text.find("t")
print(result)
#Result:2
```
Output:
```
2
```

Example 2:
```python
mystring="i love to play cricket and football"
print(mystring.find("o"))
#Result:3
```
Output:
```
3
```

Example 3:
```python
mystring="i love to play cricket and football"
print(mystring.find("cric"))
#Result:15
```
Output:
```
15
```
When you give multiple character string it will find out the starting point of string where it founds.


- if we want to find out second  occurence of of required string
```python
mystring="i love to play cricket and football"
first=(mystring.find("o")) 
second=(mystring.find("o",first+1)) 
print(second)
```
Output:
```
8
```

- If searching string not present in input string it return -1.
```python 
mystring="I am python Expert"
search=mystring.find("this")
print(search)
```
Output:
```
-1
```

### To find all occurrence of word 
```python
mystring="I am python Expert"
for i,j in enumerate(mystring):
  if j=='t':
    print(i)
```
Output:
```
7
17
```


## 6. Split()
- if you want to separate a string with white space or commas or some special character then split method is used
- **split()** method returns the list object.

```python
mystring="india pakistan china america"
#split a string with whitespace
splitstring=mystring.split(' ') #or mystring.split()
print(splitstring)
```

Output:
```
['india', 'pakistan', 'china', 'america']
```

- if you want to split a string and store its values in different variable. 
```python
mystring="india pakistan china america"
a,b,c,d=mystring.split(' ')
print(a)
print(b)
print(c)
print(d)
```

Output:
```
india
pakistan
china
america
````

## 7. join() 
- The **join()** method takes all items in an iterable and joins them into one string.
- A string must be specified as the separator.

Syntax:
```python
Sepeartor.join(iterable objects)
```

**Sepeartor**: anything that you want to use as  separator such as '-',',',''','-',  whitespaces, numbers alphabets, special characters

Example:
```python
mylist=['india', 'pakistan', 'china', 'america']
strings=','.join(mylist)
print(strings) 
```
Output:
```
india,pakistan,china,america
```

## 8. replace()
- **replace()** method replaces a specified phrase with another specified phrase.

Syntax:
```python
str.replace('old word','new word')
```
Example:
```python
stat='kat is good girl'
newstring=stat.replace('is','was')
print(newstring)
```
Output:
```
kat was good girl
```

- Replace the 'n' first occurrence of the word 'is'
Example:
```python
mystring="is he is was he in too is"
newstring=mystring.replace('is','was' ,2)
print(newstring)
```
Output:
```
was he was was he in too is
```

## For Checking Data types there are following methods are present

### 1. isalnum()
- Returns True if all characters in the string are alphanumeric:
- True if all the characters are alphanumeric, meaning alphabet letter **(a-z)** and numbers **(0-9)**.
- False if any one character from non alphanumeric value (space)!#%&?
Example
```python
mystring="Python3"
Res=mystring.isalnum()
print(Res)
```
Output:
```
True
```

### 2. isalpha()
- **isalpha()** method returns True if all the characters are alphabet letters (a-z).
- **isalpha()** method return false if one of the characters is special character or number

Example:
```python
mystring="Python3"
Res=mystring.isalpha()
print(Res)
```
Output:
```
False
```

### 3. isdecimal()
- The **isdecimal()** method returns True if all the characters are decimals (0-9).

example:
```python
mystring="\u0033" #3
res=mystring.isdecimal()
print(res)
```

Output:
```
True
```

### 4. isdigit()
- **isdigit()** method returns True if all the characters are digits, otherwise False.

Example:
```python
number="63663"
res=number.isdigit()
print(res)
```

Output:
```
True
```

### Other some remaining methods 

**isidentifier()**:
- Returns True if the string is an identifier

**islower()**:
- Returns True if all characters in the string are lower case

**isnumeric()**:
- Returns True if all characters in the string are numeric

**isprintable()**:
- Returns True if all characters in the string are printable

**isspace()**:
- Returns True if all characters in the string are whitespaces

**istitle()**:
- Returns True if the string follows the rules of a title

**isupper()**:
- Returns True if all characters in the string are upper case
