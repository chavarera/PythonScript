## Dictionary

- Dictionary holds **key: value** pair which unlike other data types that hold only single elements.
- A dictionary is a collection which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.

- **Keys** are unique within a dictionary while values may not be. 

- **values** of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

- Key-value is provided in the dictionary to make it more optimized. 

- Python Dictionary works similar to real-world Dictionary when the key element is uniques.


### How to Create a dictionary

Syntax:
```python
#Create empty dictionary
dictname=dict()

#Using {} parentheses
dictname={}

#dictionary with element 
dictname={"key1":"value1","key2":"value2"}
```

Examples:
```python
##Create empty dictionary
mydict=dict()
print("Empty Dictionary")
print(mydict)

#Dictionary with 2 element
mydict={"name":"ravi","age":20}
print("\n Dictionary with 2 Element")
print(mydict)

#dictonary with list items
mydict={"name":"ravi","age":20, "subject":["math","English"]}
print("\n Dicionary with list Element")
print(mydict)
```
Output:
```
Empty Dictionary
{}

 Dictionary with 2 Element
{'name': 'ravi', 'age': 20}

 Dicionary with list Element
{'name': 'ravi', 'age': 20, 'subject': ['math', 'English']}
```

### Accessing Key value from dictionary
 Get all keys from dictionary 
Syntax:
```python
dictname.keys()
```

Example
```python
mydict={"name":"ravi","age":20, "subject":["math","English"]}
keys=mydict.keys()
print(keys)
```
Output:
```
dict_keys(['name', 'age', 'subject'])
```


Get all values from the dictionary 

Syntax:
```python
dictname.values()
```

Example
```python
mydict={"name":"ravi","age":20, "subject":["math","English"]}
Val=mydict.values()
print(Val)
```
Output:
```
dict_values(['ravi', 20, ['math', 'English']])
```

### Accessing specific value using key
Here we can access element using the key instead of indexing.so position of key doesn't matter in the dictionary.

There are two different methods to Access element using key

**1.using normal method**

Syntax:
```python
name=dictname[key]
```

Get **ravi** from mydict using key *name*
```python
mydict={"name":"ravi","age":20, "subject":["math","English"]}
name=mydict["name"]
print(name)
```
Output:
```
ravi
```

**2.Using Built in method get()**

Syntax
```python
dictname.get(keyname)
```

Example
```python
#Dictionary
mydict={"name":"ravi","age":20, "subject":["math","English"]}

#Get Value Using key
name=mydict.get("name")
print(name)
```
Output:
```
ravi
```

### Error when you trying to Access nonexistence key
Example:
```python

mydict={"name":"ravi","age":20, "subject":["math","English"]}
#access birthdate
date=mydict["birthdate"]
```
Output:
```
KeyError: 'birthdate'
```


### Using for loop access keys and values
Example:
```python
#Simple Dictionary
mydict={"name":"ravi","age":20, "subject":["math","English"]}

#Use For Loop and Get Element using items()
for key,value in mydict.items():
  print(key,value)
```

Output:
```
name ravi
age 20
subject ['math', 'English']
```
