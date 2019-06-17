## String :abc: Methods

- Python :snake: has a set of built in methods that you can use on strings
- All string methods returns new values.they do not chnage the original string because string is immutable python object.

Following are the most common used method for strings are

## 1. capitalize() :a: :
- The **capitalize()** method upper case the first letter in the given sequences(string).

Example:
```python
text="hello"
result=text.capitalize()
print(result)
#Result:Hello
```

## 2. count() :seven: :
- The **count()** method returns the number of times a specified value appears in the string.
- Returns the frequency of given element inside string.

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
Syntax:
```python
string.count(value, start, end)
```
1. value:-	element which do you want to find count.
2. start:-	Default is 0,starting position of an element.
3. end:-	  Defualt is len(string) ,ending position of an element.

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
## 3. endswith() :speech_balloon: :

- The **endswith()** method returns True if the string ends with the specified value, otherwise False.

Example:
```python
text1="This is simple Text."
result=text1.endswith('.')
print(result)
#Result:True
````

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



## 5. find() :alembic: :
- To find out position of word or character from given string or paragraph use **find()** method.
- The **find()** method finds the first occurrence of the specified value.
- The **find()** method returns -1 if the value is not found.

Syntax
```python
string.find(str, startpoint, endpoint)
```
**str**:-which string to find
**startpoint**:-the starting  index from where you want to find string
**endpoint**:-Ending index

Example :one::
```python
text="Python"
result=text.find("t")
print(result)
#Result:2
```
Example :two:
```python
mystring="i love to play cricket and football"
print(mystring.find("o"))
#Result:3
```
Example :three: :
```python
mystring="i love to play cricket and football"
print(mystring.find("cric"))
#Result:15
```
When you give multiple character string it will find out the starting point of string where it founds.


- if we want to find out second  occurence of of required string
```python
mystring="i love to play cricket and football"
first=(mystring.find("o")) 
second=(mystring.find("o",first+1)) 
print(second)
#Result:8
```

- If searching string not present in input string it return -1.
```python 
mystring="I am python Expert"
search=mystring.find("this")
print(search)
#result:-1
```
### To find all occurrence of word :beetle:
```python
mystring="I am python Expert"
for i,j in enumerate(mystring):
    if j=='t':
         print(i)
#Result:7 17
```



## 6. Split() :frog: :
- if you want to separate a string with white space or commas or some special character then split method is used
- **split()** method returns the list object.

```python
mystring="india pakistan china america"
#split a string with whitespace
splitstring=mystring.split(' ') #or mystring.split()
print(splitstring)

#Result: ['india', 'pakistan', 'china', 'america']
```

- if you want to split a string and store its values in different variable. 
```python
mystring="india pakistan china america"
a,b,c,d=mystring.split(' ')
print(a)
print(b)
print(c)
print(d)

#Result :
'''
india
pakistan
china
america
'''
```

## 7. join() :arrows_clockwise: :
- The **join()** method takes all items in an iterable and joins them into one string.
- A string must be specified as the separator.

Syntax:
```python
Sepeartor.join(iterable objects)
```
**Sepeartor**:any thing that you want to use as  sepeartor such as '-',',',''','-',  whitespaces, numbers alphabets, special characters

Example:
```python
mylist=['india', 'pakistan', 'china', 'america']
strings=','.join(mylist)
print(strings) 
#Result:india,pakistan,china,america
```

## 8. replace() :clipboard: :
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

#Result : kat was good girl
```
- Replace the 'n' first occurrence of the word 'is'
Example:
```python
mystring="is he is was he in too is"
newstring=mystring.replace('is','was' ,2)
print(newstring)
#Result: "was he was was he in too is"
```

## For Checking Data types there are following methods are present

### 1. isalnum() :1st_place_medal: :
- Returns True if all characters in the string are alphanumeric:
- True if all the characters are alphanumeric, meaning alphabet letter **(a-z)** and numbers **(0-9)**.
- False if any one character from non alphanumeric value (space)!#%&?
Example
```python
mystring="Python3"
Res=mystring.isalnum()
print(Res)

#result: true
```

### 2. isalpha() :ab: :
- **isalpha()** method returns True if all the characters are alphabet letters (a-z).
- **isalpha()** method return false if one of the characters is special character or number

Example:
```python
mystring="Python3"
Res=mystring.isalpha()
print(Res)

#result: false
```

### 3. isdecimal() :one: :
- The **isdecimal()** method returns True if all the characters are decimals (0-9).

example:
```python
mystring="\u0033" #3
res=mystring.isdecimal()
print(res)

#result:True
```

### 4. isdigit() :moneybag: :
- **isdigit()** method returns True if all the characters are digits, otherwise False.

Example:
```python
number="63663"
res=number.isdigit()
print(res)

#result : True
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
