## Loop :loop: Statement

Python support two type of loops
1. For :boy:
2. While :girl:

### For Loop :money_with_wings:
- For loop iterate over a given sequence such as list, string, tuple dictionary or any  iterable object.
- For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.

Syntax:
```python
for variable in (iterable object) :
      print(variable)
```
Normally for range function contain three :three: different parameter
1. starting number
2. Stop number+1
3. difference or step number(optional if not given then it will increament by 1)

Example :one::
if you want to print 0 to 10 numbers using for loop
```python
for i in range(11):
     print(i)

#this will print 0,1,2...10.
```

If we do not give starting number and difference by default range function start from 0 and increament it by 1 until given number.

Example :two::
if you want to print 2 to 20 with difference 2
```python
for i  in range(2,21,2):
   print(i)

#this will print 2,4,6...20.
```
range function consider starting given no as it is (include starting number as it given ) but exclude stop number so we always provide ending number by increamenting 1.

### For Loop on String :mahjong:
if you want to print every character or alphanumeric values as one by one we can easily print using for loop.
```python
mystring="I am python student"
for st in mystring:
      print(st)
```

### For loop on List :book:
```python
mylst=[4,6,3,9,3]
for i in mylst:
      print(i)
```
### Different Example on For loop :memo:

prints out the numbers 0,1,2,3,4,5,6
```python
for x in range(7):
    print(x)
```
prints out 2,3,4,5,6,7
```python
for x in range(2, 8):
    print(x)
```
prints out 3,6,9
```python
for x in range(3, 11, 3):
    print(x)
 ```
