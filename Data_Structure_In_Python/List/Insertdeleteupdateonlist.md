## Operation  on List

As we have already know some basic of list and accessing element from it. Now today here we are going to learn insertion of new element in list, update element from list which is already available, and delete items from list.


## 1.Insertion

There are different ways to insert element in the list
```
  1. append()
  2. insert()
  3. extend()
```
### 1.append() 
**append()**  method add an element to the end of the list. 

Syntax:
```python
Lstname.append(element)
#element:any type of variable string,number, etc.. 
```
Example:
```python
color=['black','red']

#now append 'green' to list color
color.append("green") 

#now print list
print(color) 
#Result:['black','red','green']
```
Output:
```
['black','red','green']
```

#### append a another list 
Example:
```python
#initilize two list
color=['black','red']
color2=['brown','green']

color.append(color2) 

print(color)
```
Output:
```
['black','red',['brown','green']]

```
You can not append more than one element at a time using append 

This is wrong example:
```python
#initilize list
color=['black','red']

#Try to Append Two element at time
color.append('brown','green') 
```
Output Error:
```
TypeError: append() takes exactly one argument (2 given)
```

### 2.insert() 
- **append()** method is used for appending element to the end of list to overcome from this problem use insert()  method to insert an element at given particular location. 
- **insert()** method inserts the specified value at the specified position.
- if you inserting new element at 1 index position and if one element already present at 1 index position then old item position will be  right shifted by one index. 


Syntax:
```python
listname.insert(position,element) 
```
Both position and element are required element

**position**:an integer number specifying the position where to insert an item.

**element**:an element of any data type string, number, list etc... 

Example:
```python
#initilize list
color=['black','red','brown']

#insert 'green' element at 1 st position
color.insert(1, 'green') 

#print the new list
print(color)
```
Output:
```
['black','green','red','brown']
```

- while inserting element if you have give positive integer index which is not present in the current list then item will automatically added at last position. 

Example:
```python
num=[1,3,4,7]
#insert 8 element at 10th position
num.insert(10,8) 

print(num) 
```
Output:
```
[1,3,4,7,8]
```

**you can also use negative index for inserting element**
- similarly if you have give negative index which is not present in current list the item will added at 0th index

Example:
```python
#initialize num list
num=[1,3,4,7]

#insert 8 element at -10th position
num.insert(-10,8) 

print(num) 
```
Output:
```
[8,1,3,4,7]
```
### 3.extend()
**extend()**  method add the number of list element to the end of the current list

Syntax:
```python
list1.extend(lst2) 
```
Example:
```python
#initilize two list
num1=[1,3,4,7]
num2=[8, 9]

#add num2 list to num1 
num1.extend(num2) 
print(num1) 
```
Output:
```
[1,3,4,7,8, 9]
```


## 2.Delete Element

There are different ways to delete element from the list. 
```
1. del
2. pop()
3. remove()
```
### 1.del
if you removed item using del statement you cant use them for further process. 

Syntax:
```python
del list or element position
```
- if you pass list to del statement then list will completely removed from stack. 

Example:
```python
#initilize list
number=[1,3,4,7,8, 9]
#Delete 4 from above list
del number[2]

#print updated list
print(number) 
```
Output:
```
[1, 3, 7, 8, 9]
```

### How to delete list
```python
#initilize list
number=[1,3,4,7,8, 9]

#delete total list
del number

print(number) 
```
Output:
```
#Result:error because number list is deleted
#ERROR:name 'number' is not defined
```

### 2.pop()

- **pop()** method remove element from given position. 
- **pop()** method remove the element from specified position and return the deleted element value. 

Syntax
```python
listname.pop(position) 
```
Example:
```python
#initilize list
number=[1,3,4,7,8, 9]
#remove 8 element which present 4 or -2 index
del_val=number.pop(4) 

print(number) 
print(del_val)
```
Output:
```
[1, 3, 4, 7, 9]
8
``

- if you give out of range index for **pop()**  method then it will generate error saying list item out of range... 

Example
```python
number=[1,3,4,7,8, 9]
number.pop(100) 
```
Output:
```
#Result:error will occured.  pop index out of range

```

### 3.remove()
- **remove()** method remove the first occurence of of given value. 
- we can not save result of **remove()** method

Syntax;
```python
listname.remove(value) 
```

Example:
```python
#initilize list
color=['red', 'green', 'blue']

#Remove "green " From list
color.remove("green")

#print remaining list
print(color) 
```

Output:
```
['red', 'blue']
```

- If you trying to remove xyz element from list and that element is not present in the list python will generate error **"x is not in the list".**

Example:
```python
#initilize list
color=['red', 'green', 'blue']

#remove "black" From above list
color.remove("black")
````
Output:
```
Error - x is not in the list 
```

## 3.Update Element
For updating the element value 

Syntax:
```python
list[index]="new value"
```
Example:
```python
#initilize list
color=["blue","green","red"]

#update blue with *black*
color[0]="black"

#print new updated list
print(color) 
```
output:
```
["black","green","red"]
```

- If you provide out of range index while updating value then it will generate out of range index error
