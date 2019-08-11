## Set

### What is a set in Python?
- A set is a collection that is unordered and unindexed. In Python, sets are written with curly brackets(**{}**).
- Every element is unique and must be immutable (which cannot be changed). but set itself mutable objects
- Sets are unordered, so the items will appear in random order.

### How to create a set?
- you can create a set using curly braces or using built-in function **set()**.

Synatx:
```python
setname={element}
setname1=set(elements)
```
Example:
You can not create a blank set like this
```python
blankset={}
print(type(blankset)) 
```
Output:
```
<class 'dict'>
```
Create blank Set using built in function
```python
myset=set()
print(type(myset))
```
Output:
```
<class 'set'>
```

Create a set with 1,2,3,4 elements
```python
myset={1,2,3,4}
print(myset)
```
Output:
```
{1,2,3,4}
```

- Set Can not Contain any mutable object such as list
Example:
```python
my_set = {1, 2, [3, 4]}
```
Output:
```
TypeError: unhashable type: 'list'
```

### Accessing Items From a set
- You can not access Element referring by index because the set is unordered and the item has no index.
- You can use for loop for accessing the element as follows
Example:
```python
myset={1,2,3,4}
for i in myset:
    print(i)
```
Output
```
1
2
3
4
```
### Check Element present inset or not
- **in** keyword is used to check the existence of an element in the set
- Return **True** if element exists in a set otherwise Return False

Example:
```python
color={'red','green','blue'}
if('red' in color):
    print('red is present')
else:
    print('red is not found')
```
Output:
```
red is present
```

### Get the set length
Example
```python
color={'red','green','blue'}
length=len(color) 
print(length) 
```
Output:
```
3
```
