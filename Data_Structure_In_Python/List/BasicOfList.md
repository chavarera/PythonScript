## List

### Basic Of List

- A list is a collection which is ordered and changeable.
- When you create a list in Python, the python interpreter creates an array-like :office: datastructure in memory to hold your data, with your data items stacked from the bottom up. 
- list index starting from 0 and last element in the list have - 1 index

Syntax:
```python
listname=[item1, item2]
```
Example:
```python

country=['india','america','japan','china']
"""
Index of all items

positive indexs
0:india
1:america
2:japan
3:china

Negative indexes
-1:china
-2:japan
-3:america
-4:india
"""

numbers=[1,4,4,5,6,6,7]

```

### Accessing Element from list 

- Print full list :black_square_button:
```python
country=['india','america','japan','china']
print(country) 
```
Output:
```
['india','america','japan','china']
```

- Access element using index number 
To print **"india"** :earth_asia: First element from list
```python
country=['india','america','japan','china']
ind=country[0]
print(ind) 
```
Output:
```
india
```
- Print last element from list 
```python
country=['india','america','japan','china']
ind=country[-1]
#Or
Ind=country [3]
print(ind) 
```

Output:
```
china
```


### list index out of range 

- If you are trying to accessing element with a invalid  index or out range index 
Then it will give list index out of range

Example:
```python
numbers=[1,4,4,5,6,6,7]
res=numbers[56]
```
output:
```
res=numbers[56]
IndexError: list index out of range
```

### Accessing multiple element from list 
- For accessing multiple element from given list we can use slicing similar to string as follows

Example:
To print america, japan
```python
country=['india','america','japan','china']
res=country[1:3]
print(res) 
```
Output:
```
['america','japan']
```

### Nested List
- we can add a another list inside a list as follows

Example
```python
numbers=[1,4,4,5,6,6,7,[8,9],[10,11]]
```

### Accessing Element from nested list
Example
```python
numbers=[1,4,4,5,6,6,7,[8,9],[10,11]]

#To get 8
res=numbers[7][0]
print(res)

#To access 11
res=numbers[8][1]
print(res)
```
Output:
```
8
11
```

## Get the length of item available in list
- **len()**  method is used 

Example:
```python
numbers=[1,4,4,5,6,6,7]
res=len(numbers) 
print (res) 
```
Output:
```
7
```

### Copy  a list into another list
- You cannot copy a list simply by typing *list2 = list1*, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
- There are two different ways to make a copy of list

**1.copy()** :wavy_dash:
 
 create copy of list using **copy()** method

Example:
```python
numbers1=[1,4,4,5,6,6,7]
numbers2=numbers1.copy() 
print(numbers2) 
```
Output:
```
[1,4,4,5,6,6,7]
```

**2.list()**

create copy of list using **list()** method
```python
numbers1=[1,4,4,5,6,6,7]
numbers2=list(numbers1) 
print(numbers2) 
```
Output:
```
[1,4,4,5,6,6,7]
```
