## Basic operation on dictionary


### 1. Add new key-value element in the dictionary

 we can add key and value in a dictionary using the key.

Syntax:
```python
dictname[key]=value
```
Example:
```python
mydict={"name":"ravi","age":20}
mydict["bdate"]="26/01/1993"

print(mydict)
```
Output:
```
{"name":"ravi","age":20,"bdate":"26/01/1993"}
```


### 2. Updating value in dictionary
Syntax:
```python
dictname[existed key]="new value"
```

Example:
```python
mydict={"name":"ravi","age":20}
#update name with jhon

mydict["name"]="jhon"

print(mydict)
```
Output:
```
{"name":"jhon","age":20}
```

### 3. Removing key-value pair from the dictionary

use built in method **pop()** to remove element from dictionary

Syntax:
```python
dictname.pop("keyname")
```

Example:
```python
mydict={"name":"ravi","age":20}
#remove age
mydict.pop("age")

print(mydict)
```
Output:
```
{"name":"ravi"}
```

### 4. Clear all element of the dictionary

**clear()** is a built-in method used to empty the dictionary.

Syntax:
```python
dictname.clear()
```

Example:
```python
mydict={"name":"ravi","age":20}
#clear all element 
mydict.clear()

print(mydict)
```
Output:
```
{}
```

### 5. Deleting dictionary
**del** keyword used to delete complete dictionary.

Syntax:
```python
del dictionary_name
```
Example
```python
mydict={"name":"ravi","age":20}
del mydict
print(mydict)
```
Output:
```
NameError: name 'mydict' is not defined
```
