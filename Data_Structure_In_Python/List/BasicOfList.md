## List :page_with_curl:

### Basic Of List

- A list is a collection which is ordered and changeable :black_nib:. 
- When you create a list in Python :snake:, the python interpreter creates an array-like :office: datastructure in memory to hold your data, with your data items stacked from the bottom up. 
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

### Accessing Element from list :ticket:

- Print full list :black_square_button:
```python
country=['india','america','japan','china']
print(country) 
#Result:['india','america','japan','china']
```
- Access element using index number :one:
To print **"india"** :earth_asia: First element from list
```python
country=['india','america','japan','china']
ind=country[0]
print(ind) 
#Result:india
```
- Print last element from list :end:
```python
country=['india','america','japan','china']
ind=country[-1]
#Or
Ind=country [3]
print(ind) 
#Result:china
```

### list index out of range :warning:

- If you are trying to accessing element with a invalid :no_entry: index or out range index 
Then it will give list index out of range

Example:
```python
numbers=[1,4,4,5,6,6,7]
res=numbers[56]

#Result:Error-list index out of range
```
### Accessing multiple element from list :diamond_shape_with_a_dot_inside:

- For accessing multiple element from given list we can use slicing similar to string as follows

Example:
To print america, japan
```python
country=['india','america','japan','china']
res=country[1:3]
print(res) 
#Result:['america','japan']
```
### Nested List :loop:
- we can add a another list inside a list as follows

Example
```python
numbers=[1,4,4,5,6,6,7,[8,9],[10,11]]
```

### Accessing Element from nested list :nut_and_bolt:
Example
```python
numbers=[1,4,4,5,6,6,7,[8,9],[10,11]]

#To get 8
res=numbers[7][0]

#To access 11
res=numbers[8][1]
```

## Get the length  :straight_ruler: of item available in list
- **len()**  method is used 

Example:
```python
numbers=[1,4,4,5,6,6,7]
res=len(numbers) 
print (res) 
#Result:7
```
### Copy :beginner: a list into another list
- You cannot copy a list simply by typing *list2 = list1*, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
- There are two different ways to make a copy of list

**1.copy()** :wavy_dash:
 
 create copy of list using **copy()** method

Example:
```python
numbers1=[1,4,4,5,6,6,7]
numbers2=numbers1.copy() 
print(numbers2) 
#Result:[1,4,4,5,6,6,7]
```

**2.list()** :book:

create copy of list using **list()** method
```python
numbers1=[1,4,4,5,6,6,7]
numbers2=list(numbers1) 
print(numbers2) 
#Result:[1,4,4,5,6,6,7]
```
