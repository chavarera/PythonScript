## String Methods

- Python has a set of built in methods that you can use on strings
- All string methods returns new values.they do not chnage the original string because string is immutable python object.

Following are the most common used method for strings are

### 1. capitalize():
- The **capitalize()** methodupper case the first letter in the given sequences.

Example:
```python
text="hello"
result=txt.capitalize()
print(result)
#result:Hello
```

### 2. count():
- The **count()** method returns the number of times a specified value appears in the string.
Example:
```python
text1="Hello"
result=text1.count('l')
result1=text1.count('H')

print(result) #result:2
print(result1) #result:1

```
Syntax:
```python
  string.count(value, start, end)
  #value	Required. A String. The string to value to search for
  #start	Optional. An Integer. The position to start the search. Default is 0
  #end	Optional. An Integer. The position to end the search. Default is the end of the string
```
For Example
```python
text1="This is simple Text"
result=text1.count('i')
res=text1.count('i',6,len(text1))
print(result) #result:3
print(res) #result :1
```

