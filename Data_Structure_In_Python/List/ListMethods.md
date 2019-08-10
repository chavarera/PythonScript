## List Methods

### 1.clear()
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
Output:
```
[1, 2, 3, 4, 5]
[]
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
Output:
```
5
```

If string search value put quotes inside count method
Example:
```python
color=["red","blue","green","red","yello","orange","red"]
#find out count of red
red_cnt=color.count("red") 
print(red_count) 
#Result:3
```
Output:
```
3
```

#### count list inside a list
```python
lst=[1, 2,3,4,5,1,4,1,1,1,[8,9]]

cnt=lst.count([8,9])
print(cnt) 
#Result:1
```
Output:
```
`
```

### 3.index()

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
Output:
```
0
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
```
Output:
```
[4,8,7,5]
```

Example 2:
```python
color=["red","blue","green"]
color.reverse() 
print(lst) 
```
Output:
```
["green","blue","red"]
```

Once you apply **.reverse()** on the list you can not get back original list

 **reversed()**
- The buil-in function **reversed()** returns a reversed iterator object.

Example:
```python
color=["red","blue","green"]
print("reversed list",list(reversed(color))) 
print("original list ",color) 
#Result:
#reversed list ["green","blue","red"]
#original list   ["red","blue","green"]

```
Output:
```
reversed list ['green', 'blue', 'red']
original list  ['red', 'blue', 'green']
```

### 5.sort() :chart_with_upwards_trend:
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
```
Output:
```
[1,2,3,4,5,6]
```

Sort descending
```python
lst=[4,3,5,2,1,6]
lst.sort(reverse=True) 
print(lst) 
```
Output:
```
[6,5,4,3,2,1]
```
**Note**: After sorting done using **.sort()** method you can not get original list back all position of all element changed we can not recover it. 

**sorted()** :bar_chart:
- Sorting any sequence is very easy in Python using the built-in method sorted() which does all the hard work for you.

- Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in a sorted manner, without modifying the original sequence.

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
Output:
```
[1, 2, 3, 4, 5, 6]
[4, 3, 5, 2, 1, 6]
```
