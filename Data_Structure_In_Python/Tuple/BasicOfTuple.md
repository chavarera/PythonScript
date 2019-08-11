## Tuple

### Basic Of Tuple
- A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
- A tuple is a collection that is ordered and unchangeable. In Python, tuples are written with round brackets. 
- Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

Syntax:
```python
tuplename=(elem1,elem2,elem3...) 
```

Example:
```python
color=("red","blue","green")
print(color)
```

Output:
```
('red', 'blue', 'green')
```

- Create A blank Tuple
```python
blanktuple=() 
#you can also use 
blanktuple=tuple()

#Print the type of above object
print(type(blanktuple))
```
Output:
```
<tuple class>
```

To write a tuple containing a single value you have to include a comma, even though there is only one value

Example:
```python
tupl1=(4,) 
print(tupl1)
```
Output:
```
(4,)
```

- Create A tuple with 7 element
```python
elements=(1,2,3,4,5,6,7) 
#printing the Element
print(elements) 
```
Output:
```
(1,2,3,4,5,6,7)
```



### Access Tuple Items

- As an ordered sequence of elements, each item in a tuple can be called individually, through indexing.
- Each item corresponds to an index number, which is an integer value, starting with the index number 0.
- You can access tuple items by referring to the index number, inside square brackets

Syntax:
```python
tuplenmae[index]
```
Example:
```python
mytuple=(2,4,5,67) 
print("Tuple Element")
print(mytuple)

#get 5 element 
res=mytuple [2]
print("Element at index 2")
print(res)
#Result:5
```
Output:
```
Tuple Element
(2, 4, 5, 67)
Element at index 2
5
```

### Access Multiple elements from a tuple
We can use indexing to call out a few items from the tuple. Slices allow us to call multiple values by creating a range of index numbers separated by a colon [x:y].

we can use slicing to accessing elements from the tuple. 

Synatx:
```python
tuplename[startpostion:endposition]
```

Example:
```python
mytuple=(1,3,4,5,6,7,8,9) 
res=mytuple[2:7]
print(res) 
```
Output:
```
(4,5,6,7,8,9) 
```


### Extended slicing
- The syntax for this construction is **tuple[x:y:z]**, with z referring to stride. Let’s make a larger list, then slice it,

Example:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) 
print(numbers[1:11:2])
```
Output:
```
(1, 3, 5, 7, 9)
```
- We can omit  the first two parameters and use stride alone as a parameter with the syntax **tuple[::z]**

Example:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) 
print(numbers[::3])
```
Output:
```
(0, 3, 6, 9, 12)
```
