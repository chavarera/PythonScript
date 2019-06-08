## Operation on Tuple :eyeglasses:

### 1.Concatenating 2 tuples :school_satchel:

Example:
```python
tupl1=(1, 3) 
tupl2=("red","green") 

tupl3=tupl1+tupl2
print(tupl3) 

#result:(1, 3,"red", "green") 
```

### 2.Nested tuple :loop:

Example:
```python
tupl1=(1, 3) 
tupl2=["red","green"]

tupl3=(tupl1,tupl2) 
print(tupl3) 

#result:((1, 3),["red", "green"]) 
```

### 3. Change Tuple value :electric_plug:

- unlike list, tuple are immutable objects. This means that elemnt of tuple can not be changed once it has been assigned. 
- but if tuple contain any mutable object such as list then this object can be changeable. 

For Example:
```python
 mytple=(1,2,3,4,5,["red", "green"]) 
# change 2 element with 9
mytple[1]=9
#Result:Error tuple object does not support item assignments
````

But in same example you want to replace **"red"** With **"black"**

Example:
```python
mytple=(1,2,3,4,5,["red", "green"]) 
# change "red"  element with "black"
mytple[5][1]="black"

print(mytple) 
#result:(1,2,3,4,5,["black", "green"]) 
```

### 4. Deleteing Tuple :no_entry:
- Tuple is immutable object so we can delete individual item from tuple. 
- Entire tuple will be deleted or removed  using del keyword. 

Syntax:
```python
del tuplename
```
Example:
```python
mytple=(1,2,3,4,5,["red", "green"]) 
# delete tuple

del mytple
print(mytple)
#Error mytple is not defined
```


### 5. Counting Frequencey of Element
- get the frequency of particular element appears in tuple

Synatx:
```python
tuplename.count(element) 
```
Example:
```python
tpl=(3,4,68,3,5,3) 
res=tpl.count(3)
print(res) 
#Result:3
```

### 6. Find Position index of element :mag_right:.

- get the first index of specified value. 

Syntax:
```python
tuplename.index(value) 
```
Example:
```python
tpl=(3,4,68,3,5,3,4) 
res=tpl.index(4)
print(res) 
#Result:1
```

### 7.Check element is present in tuple or not :mag:

- **'in'** keyword is used to check whether element is present in tuple or not
- if element is present this will return boolean value True otherwise False

Syntax:
```python
Element in tuplename
```
Example:
```python
tpl=(3,4,68)
# check 4 is present or not
if 4 in tpl:
    print("present") 
else:
    print("Not present")
```
