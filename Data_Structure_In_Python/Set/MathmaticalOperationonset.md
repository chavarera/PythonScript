## Set Operation :wrench:

Sets can be used to carry out mathematical set operations following different operation on set can be performed 

1. Union (|)
2. Intersection (&)
3. difference (-)
4. symmetric difference (^)

![Basic operation](https://www.sketch.com/images/pages/docs/04-shapes/operations.jpg)

### 1.union() :briefcase:
- Two sets can be **added** together.
- Union is performed using | operator same can be achived using built in function **union()**.

Syntax:
```python
setA=set()
SetB=set()
#Using | Operator
result=SetA | SetB 

#Using Built in Function .union()
result=SetA.union(SetB)
```

Example:
```python
#Initialize Two Set
A={1,5,2}
B={6,7,8,9}

#using built in method .union()
result=A.union(B)
print(result)
#Result:{1, 2, 5, 6, 7, 8, 9}

#Using | operator
result1=A | B
print(result1)
#Result:{1, 2, 5, 6, 7, 8, 9}
```


### 2.Intersection  :x:
- A new set can also be constructed by determining which members two sets have **in common**.
- Intersection is performed using **&** operator same can be achived using built in function **intersection()**.

Syntax:
```python
setA=set()
SetB=set()

#Using & operator
result=SetA & SetB 

#using intersection() method
result=SetA.intersection(SetB)
```

Example:
```python
#Initialize Two Set
A={1,5,2}
B={3,2,1,6,8,7}

#using built in method .intersection()
result=A.intersection(B)
print(result)
#Result:{1, 2}

#Using & operator
result1=A & B
print(result1)
#Result:{1, 2}
```

### 3. Difference :no_entry:
- Two sets can also be **subtracted**.
- Difference can be performed using **-** operator or same thing can be achieved using **difference()**.
- Here **A-B** Result is Different result than **B-A**.

**A-B**:The elements included in A, but not included in B.
**B-A**:The elements included in B, but not included in A.

Syntax:
```python
setA=set()
SetB=set()

#using - Operator
result=SetA - SetB 

#Using .difference()
result=SetA.difference(SetB)
```

Example:
```python
A={1,2,3,5,4}
B={2,4,8,6,9}

#using built in method .difference()
result=A.difference(B)
print(result)
#Result:{1, 3, 5}

#Using - operator
result1=A - B
print(result1)
#Result:{1, 3, 5}
```


### 4. symmetric Difference :no_entry_sign:
- The **symmetric_difference()** method returns a set that contains all items from both set, but not the items that are present in both sets.
- symmetric Difference can be performed using **^** operator or same thing can be achieved using **symmetric_difference()**.

Syntax:
```python
setA=set()
SetB=set()

#Using ^ Operator
result=SetA ^ SetB 

#Using symmetric_difference()
result=SetA.symmetric_difference(SetB)
```


Example:
```
#Initialize Two Diffrent Sets
A={1,2,3,5,4}
B={2,1,8,6,9}

#using built in method .symmetric_difference()
result=A.symmetric_difference(B)
print(result)
#Result:{3, 4, 5, 6, 8, 9}

#Using ^ operator
result1=A ^ B
print(result1)
#Result:{3, 4, 5, 6, 8, 9}
```
