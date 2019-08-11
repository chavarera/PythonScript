## Built-in Function For tuple
There are the number of built-in functions are available to process tuple

### 1.length
- **len()** function is used to return number of elements inside in tuple.

Syntax:
```python
len(tuplename)
```
Example:
```python
mytuple=(1,2,3,5,4,8,4)

#length of tuple
res=len(mytuple)

print("Length Of Tuple")
print(res)    
```
Output:
```
7
```

### 2.max()
- The **max()** method returns the largest element in an iterable or largest of two or more parameters.
Syntax:
```python
max(iterable, *iterables[,key, default])
max(arg1, arg2, *args[, key])
```

Example:
```python
mytuple=(1,2,3,5,4,8,4)
#Get Maximum High Element
res=max(mytuple)
print("Max Element")
print(res)
```
Output:
```
Max Element
8
```

### 3.min()
- The **min()** method returns the smallest element in an iterable or largest of two or more parameters.
Syntax:
```python
min(iterable, *iterables[,key, default])
min(arg1, arg2, *args[, key])
```    

Example:
```python
mytuple=(1,2,3,5,4,8,4)

#Get Minimum Amount
res=min(mytuple)
print("Min Element")

print(res)
```
Output:
```
1
```

### 4.any()
- Return True if any element of the iterable is true
- If the iterable is empty, return False.

Examples:
```python
# all values are true
tupl1 = (5, 8, 9, 4)
print(any(tupl1))
#Result:True

# all values are false
tupl2 = (0, False)
print(any(tupl2))
#Result:False

# one value is false, others are true
tupl3 = (0, 8, 18, 5)
print(any(tupl3))
#Result:True

# one value is true, others are false
tupl4 = (55, 0, False)
print(any(tupl4))
#Result:True

# empty iterable
tupl5 = ()
print(any(tupl5))
#Result:False
```
Output:
```
True
False
True
True
False
```

### 5.all()
- Return True if all elements of the iterable are true (or if the iterable is empty)


Examples:
```
# all values are true
tupl1 = (5, 8, 9, 4)
print(any(tupl1))
#Result:True

# all values are false
tupl2 = (0, False)
print(any(tupl2))
#Result:False

# one value is false, others are true
tupl3 = (0, 8, 18, 5)
print(any(tupl3))
#Result:False

# one value is true, others are false
tupl4 = (55, 0, False)
print(any(tupl4))
#Result:False

# empty iterable
tupl5 = ()
print(any(tupl5))
#Result:True
```
Output:
```
True
False
True
True
False
```
