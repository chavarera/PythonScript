## Tuple :game_die:

### Basic Of Tuple :snowboarder:
- A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
- A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. 
- Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

Syntax:
```python
tuplename=(element by comma separtor) 
```
Example:
```python
color=("red","blue","green")
```

- Create A blank Tuple :pill:
```python
blanktuple=() 
#you can also use 
blanktuple=tuple()

#Print the type of above object
print(type(blanktuple))

#Result:<tuple class>
```

- To write a tuple containing a single value you have to include a comma, even though there is only one value

Example:
```python
tuple1=(4,) 
```

- Create A tuple with 5 element
```python
elements=(1,2,3,4,5,6,7) 
#printing the Element
print(elements) 

#Result:(1,2,3,4,5,6,7)
```


### Access Tuple Items :wrench:

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
#get 5 element 
res=mytuple [2]
#Result:5
```

### Access Multiple :cookie: element from tuple
- We can use indexing to call out a few items from the tuple. Slices allow us to call multiple values by creating a range of index numbers separated by a colon [x:y].
- we can use slicing to accessing elements from tuple. 

Synatx:
```python
tuplename[startpostion:endposition]
```

Example:
```python
mytuple=(1,3,4,5,6,7,8,9) 
res=mytuple[2:7]
print(res) 
#Result:(4,5,6,7,8,9) 
```


### Extended slicing :scissors:
- The syntax for this construction is tuple[x:y:z], with z referring to stride. Let’s make a larger list, then slice it,

Example:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) 
print(numbers[1:11:2])
#Result:(1, 3, 5, 7, 9)
```
- We can omit :name_badge: the first two parameters and use stride alone as a parameter with the syntax tuple[::z]

Example:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) 
print(numbers[::3])
#Result:(0, 3, 6, 9, 12)
```
