## List comprehension  :bookmark_tabs:

### Introduction
- List comprehension Help :snowman: us to reduce number of line code :scroll:. 
- List comprehension is generally more compact and faster :runner: than normal functions and loops :loop: for creating list.
- List comprehensions are used for creating new lists from other iterables.
- List comprehension :moneybag: is an elegant way to define and create lists based on existing lists.

Syntax:
```python
Newlist=[expression(item) for item in list]
```
Example:

Create a list which contains 1 to 10 number 

Using normal for loop
```python
#initilize empty list
lst=[]
for i in range(1, 11) :
      lst.append(i) 
print(lst) 
#Result:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Now using list comprehension :moneybag:
```python
#using List comprehension
lst=[i for i in range(1,11)]
print(lst) 
#Result:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### list comprehension using conditions :wrench:

Syntax:
```python
Newlist=[expression(item) for item in list conditions]
```

Example:
Create a list which contains
2,4,6,8,10

Normal for loop
```python
#blank list
lst=[]
for i  in range(11) :
    if i%2==0:
        lst.append(i) 
print(lst) 
#Result:[0, 2, 4, 6, 8, 10]
```
Using List comprehension
```python
#using List comprehension
lst=[i for i in range(11)  if i%2==0]
print(lst) 
#Result:[0, 2, 4, 6, 8, 10]

```
You can achieve above sequence using **range(2,11,2)** also. But we need to understand conditional statement inside list comprehension so we use normal range function. 


### If else :bomb: in list comprehension. 
Example:
Find out even or odd number from 1 to 10

Using normal for loop
```python
lst=[]
for i in range(1,11):
      if i%2==0:
          lst.append("Even")
      else:
          lst.append("odd") 
print(lst) 
#Result:['odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even']
```
Using list comprehension
```python
lst=["Even" if i%2==0 else "odd" for i in range(1,11)]
print(lst) 
#Result:['odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even']
```

### Error :no_entry_sign: In List Comprehenstion

expression in list comprehension can only accept single variable of any type(string,list,int,tuple) 
object we can not add element more than one

Example 
```python
lst=[i,i*2 for i in range(5)]
#Result:invalid syntax
```
This will always generate error **Invalid syntax** :microscope:

Correct way
```python
#using Tuple
lst=[(i,i*2) for i in range(5)]
print(lst)
#Result:[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)]


#Using List
lst=[[i,i*2] for i in range(5)]
print(lst)

#Result:[[0, 0], [1, 2], [2, 4], [3, 6], [4, 8]]
```

**Note** :black_nib:
every list comprehension can be rewritten in for loop, 
but every for loop can’t be rewritten in the form of list comprehension.
