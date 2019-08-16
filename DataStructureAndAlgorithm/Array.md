## Array

#### Introduction
- The array is the most commonly used data structure in most of the programming languages.
- The collection of elements of the same data types grouped together called is an array.
- All elements of an array must be of the same datatypes.
- We can create an array in python by importing an array module.
- In Python list treated as an array but the list contains a different type of element inside it where array support only a single type of element to be stored in it.

#### How to create Array?
First import array module as follows
```python
import array
```
Create an array using array module
```python
array=array.array('singletypecode',[element of similar data types])
```

- If you pass different type element to array it will generate an error
- Arrays represent basic values and behave very much like lists

**Applications of An Array**
 1. lookup table
 2. hash table
 3. heaps


**Advantages of an Array**
- Very easy to implement and use.
- Fast data structure
- Any item from any position can be accessed because of indexes are present in an array
- arrays can have as many dimensions as we want 
- The size of the array can be changed dynamically.

**Disadvantages of an Array**
- Store only similar data types item in the array

Examples:
```python
#import array module
import array

#Create a integer elements array
arr=array.array('i',[1,2,3,4,5,6,7])

#print array
print("Normal Array")
print(arr)

#print type of an array
print("\n Type of an Array")
print(type(arr))
```
Output:
```
Normal Array
array('i', [1, 2, 3, 4, 5, 6, 7])

 Type of an Array
<class 'array.array'>
```
