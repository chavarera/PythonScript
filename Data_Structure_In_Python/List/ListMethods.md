## List Methods

### 1.clear() :no_entry:
- **clear()** method removes all the elements from a list.

Syntax:
```python
listname.clear() 
```
Example:
```python
lst=[1, 2,3,4,5]
print(lst) 
#Result:[1, 2,3,4,5]

#Now clear the list using clear() 
lst.clear() 
print(lst) 
#Result:[]
```

### 2. count() :100:
- **count()** method returns the number of elements with the specified value.
- Any type of  (string, number, list, tuple, etc.)  Data can be counted using count() method. 

Syntax:
```python
lstname.count(value) 
```
Example:
```python
lst=[1, 2,3,4,5,1,4,1,1,1]
cnt=lst.count(1)
print(cnt) 
#Result:5
```

If string search value put quotes inside count method
Example:
color=["red","blue","green","red","yello","orange","red"]
#find out count of red
red_cnt=color.count("red") 
print(red_count) 
#Result:3

#### count list inside a list :loop:
```python
lst=[1, 2,3,4,5,1,4,1,1,1,[8,9]]

cnt=lst.count([8,9])
print(cnt) 
#Result:1
```

### 3.index() :one:

- **index()** method return the position index of specified value.
-  **index()** method returns the position at the first occurrence of the specified value

Syntax:
```python
listname.index(value) 
```
Example:
```python
color=["red","blue","green"]
indx=color.index("red")
print(indx) 
#Result:0
```

### 4. reverse() :end:
- **reverse()** method reverses the given elements from list.

Syntax:
```python
listname.reverse() 
```

Example 1:
```python
lst=[5,7,8,4]
lst.reverse() 
print(lst) 
#Result:[4,8,7,5]
```

Example 2:
```python
color=["red","blue","green"]
color.reverse() 
print(lst) 
#Result:["green","blue","red"]
```
Once you apply **.reverse()** on list you can not get back original list

 **reversed()**
- The buil-in function **reversed()** returns a reversed iterator object.

Example:
```python
color=["red","blue","green"]
print("reversed list",reverse(color)) 
print("original list ",lst) 
#Result:
#reversed list ["green","blue","red"]
#original list   ["red","blue","green"]
```

### 5.sort()
- **sort()**  method sort the list in ascending and descending order
- **sort()** method sorts the list ascending by default.

Synatx:
```python
listname.sort(reverse=True|False, key=myFunc) 
```
Example:
Sort ascending
```python
lst=[4,3,5,2,1,6]
lst.sort() 
print(lst) 
#Result:[1,2,3,4,5,6]
```
Sort descending
```python
lst=[4,3,5,2,1,6]
lst.sort(reverse=True) 
print(lst) 
#Result:[6,5,4,3,2,1]
```
**Note**: After sorting done using **.sort()** method you can not get original list back all position of all element changed we can not recover it. 

**sorted()** :bar_chart:
- Sorting any sequence is very easy in Python using built-in method sorted() which does all the hard work for you.

- Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in sorted manner, without modifying the original sequence.

Syntax:
```python
sorted(iterable object, key, reverse=True/False)
```

Example:
```python
lst=[4,3,5,2,1,6]
print(sorted(lst)) #sorted list
#Result:[1,2,3,4,5,6]

#print original list
print(lst) 
#Result:[4,3,5,2,1,6]
```
