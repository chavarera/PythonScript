## Array Operations

### 1.Retrieve element

for Retrieving elements from an array, there are two different ways

1. Single element Retrieval
2. Multiple elements retrieval using slicing.


#### 1. Single Element Retrieval

- A collection of elements each identified by an array index.
- Index start at zero(0) array.Because of the index, random access of element is possible.
- Use [] parenthesis to retrieve an element from an array
- Array elements can be accessed using positive index start from the first element in the array
```
like 0,1,2,3,4...
```
- Array elements also can be accessed using negative indexes which start from ending of the list 
```
like -1,-2,-3,-4..
```

Syntax:
```python
array_name[index]
```

Example:
```python
import array

data=array.array("i",[20,10,15,23])

#for 20 use 0 index to get value from it
result=data[0]
print(result)
#Result:20

#Access 20 using negative index
result=data[-4]
print(result)
#Result:20


#for 15 use 2 index to get value from it
result=data[2]
print(result)
#Result:15

#for 15 using Negative index
result=data[-2]
print(result)
#Result:15

#For outer index 
result=data[10]
print(result)
#Result Error: array index out of range
```

#### 2.Multiple Elements using slicing

- In Python, we can easily access a range of items in an array using slicing operator :

Normal Syntax:
```python
array_name[startindex(including):EndIndex(Excluding)]
```

Other Syntax :
```python
array_Name[:]		-> All Elements
array_name[start:end]	-> Begining to End
array_name[:end]	-> Begining to end
array_name[start:]	-> begining to end
```

Examples:
```python
import array

data=array.array("i",[20,10,15,23])

#ALL Elements
start=0
end=4

result=data[start:end]
print(result)
#Result:array('i', [20, 10, 15, 23])

#Get First 2 Elements
result=data[:2] #or data[0:2]
print(result)
#Result:array('i', [20, 10])

#Get Last 3 Elements
result=data[1:] #or data[1:3]
print(result)
#Result:array('i', [10, 15, 23])
```


### 2.Add Element

- After the creation of the array, we can add another element to array with the help of following built-in functions

1. append()
2. insert()
3. extend()

#### 1.append()
- **append()** function add a single element to an array at the end of the array

Syntax:
```python
arrayName.append("element")
```

Examples:
```python
import array

data=array.array("i",[20,10,15,23])
print("Before append of new Element")
print(data)


#Append 6 to the data array
data.append(6)
print("After appending element")
print(data)

'''
#Result

Before append of new Element
array('i', [20, 10, 15, 23])

After appending element
array('i', [20, 10, 15, 23, 6])
'''
```

#### 2.insert()

- **append()** add elements at only end of the array but if you want to add an element at the specific position then use insert.
- if an element is already present at insertion position then element at insertion position will be shifted to the right side by one.
- If you pass out of range positive index then element should be added at the end of an array.
- If you pass out of range negative index then element should be added at the beginning of an array.

Syntax:
```python
array_name.insert(index,"value")
```
Example:
```python
import array

data=array.array("i",[20,10,15,23])
print("Normal Array")
print(data)


#Append 6 at 1th position
data.insert(1,6)
print("After inserting 6  at first position element")
print(data)

'''
#Result

Normal Array
array('i', [20, 10, 15, 23])'


After inserting 6  at first position element
array('i', [20, 6, 10, 15, 23])
'''
```

#### 3.extend()

- **append()** and **insert()** function add single element to an array to add multiple element to an array or join two different array extend() built in function is is used
- Add several items using **extend()** method.
- **extend()** appends iterating to the end of the array

Syntax:
```python
array_name.extend(iterable_object)
```
**iterable_object**:list,tuple


Example:
```python
import array

data=array.array("i",[20,10,15,23])
print("Normal Array")
print(data)


#add  [6,11,12] array to data array
data.extend([6,11,12])

print("\n\n Array After Extending [6,11,12] ")
print(data)

'''
#Result:
Normal Array
array('i', [20, 10, 15, 23])

Array After Extending [6,11,12] 
array('i', [20, 10, 15, 23, 6, 11, 12])
''' 
```

### 3.Update Element

- The array is the mutable object. so elements of an array are changeable

Syntax:

To change or modify an element of an array use index of that element
```python
array_name[index]=value
```

To modify some range of elements from an array
```python
array_name[startindex:endindex]=value
```

Example:
```python
import array

data=array.array("i",[20,10,15,23])
print("Normal Array")
print(data)

#update 20 with 30 and 20 element at 0 index
data[0]=30
print("\nArray after modification of 20 with 30")
print(data)

#Update last 2 element 9 and 12
data[-2:]=array.array('i',[9,12])
print("\nArray After updating multiple values")
print(data)
'''
#Result
Normal Array
array('i', [20, 10, 15, 23])

Array after modification of 20 with 30
array('i', [30, 10, 15, 23])

Array After updating multiple values
array('i', [30, 10, 9, 12])
'''


'''
data[0]='h'
This will generate error
Erro:an integer is required (got type str)


data[552]='1'
Error:array assignment index out of range
'''
```

### 4. Remove Element

- You can delete complete array or element there are following options are available.
1. del
2. pop()
3. remove()


#### 1.del
- We can delete one or more items using python del statement.
- we can also delete complete array using del keyword.

Syntax:

delete of specific index item
```python
del array_name[index]

```
Delete Complete array
```python
del array_name
```
Examples:
```python
import array

data=array.array("i",[20,10,15,23])
print("Normal Array")
print(data)

#Delete the first Element from an array
del data[0]

print("\n AFter delete first element")
print(data)

#delete complete array
del data

print(data)
#result:name 'data' is not defined

'''
Normal Array
array('i', [20, 10, 15, 23])

AFter delete first element
array('i', [10, 15, 23])
'''
```

#### 2.pop()

- **pop()** method used to remove an item at the given index.
- **pop()** also return an item which is deleted

Syntax:
```python
array_name.pop(index)
```

Example:
```python
import array

#Normal Array
arr=array.array('i',[20, 10, 15, 23])

#print Normal Array
print(arr)

#Delete last Element
arr.pop()


#print array after pop
print(arr)

'''
#Result
array('i', [20, 10, 15, 23])
array('i', [20, 10, 15])
'''
```

#### 3.remove()

- We can use the remove() method to remove the given item.
- **remove()** method accept element instead of the index.
- **remove()** method removes an element from an array and doesn't return anything
- If the element not found in list **remove()** gives an error
```
x not in the list
```

Syntax:
```python
array_name.remove(elements)
```
Example:
```python
import array

data=array.array("i",[20,10,15,23])
print("Normal Array")
print(data)

#Remove 10 from an array using remove()
data.remove(10)


print("\n Print array after remove of 10")
print(data)

'''
Normal Array
array('i', [20, 10, 15, 23])

Print array after remove of 10
array('i', [20, 15, 23])
'''
```
