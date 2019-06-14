## Basic operation on dictionary


### 1. Add new key value element in dictionary

 we can add key and value in dictionary using key.

Syntax:
```python
dictname[key]=value
```
Example:
```python
mydict={"name":"ravi","age":20}
mydict["bdate"]="26/01/1993"

print(mydict)
#Result:{"name":"ravi","age":20,"bdate":"26/01/1993"}
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
#Result : {"name":"jhon","age":20}
```

### 3. Removing key value pair from dictionary

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
#Result:{"name":"ravi"}
```

### 4. Clear all element of dictionary

**clear()** in built method is used to empty the dictionary.

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
#Result:{}
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
#Result:mydict is not defined
