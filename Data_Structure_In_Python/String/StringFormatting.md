## String Formating 

### Basic of String Formatting
- String Formatting is one good way to joins and combines two or more string with different data.
- Formats specified values in a string.
- **format()**  string method is used for string Formating.

### Using .format() we can archives different things

### 1.String concatenation 
Syntax
```python
'{}  {}'.format(list of variables)
```

for example, if we want to write **" value is 10"**

Normal way to write
```python
a=10
print('value is '+str(a))
```
Output:
```
value is 10
```

Using String Formatting
```python
a=10
print('value is {}'.format(a))
```
Output:
```
value is 10
```

if we want to print **"a value is 10 and b value is 20 and c value is 39"**

Normal way
```python
a=10
b=20
c=39
res='a value is '+str(a)+' and b value is '+str(b)+' and c value is '+str(c)
print(res)
```

Output:
```
a value is 10 and b value is 20 and c value is 39
```

Using string Formatting
```python
a=10
b=20
c=39
print('a value is {} and b value is {} and c value is {}'.format(a,b,c))
```
Output:
```
a value is 10 and b value is 20 and c value is 39
```

- You can also give position inside {} block like {1} then this will get value from **.format(0position,1position,2postion)**
```python
a=10
b=20
c=39
print('a value is {2} and b value is {1} and cvalue is {0}'.format(a,b,c))
```
Output:
```
a value is 39 and b value is 20 and cvalue is 10
```
- here **{2}** get value from the format and get value whose position is 2 in formatting.

- We can also use variable name inside a braces also as following
```python
a=10
b=20
c=39
v='a value is {a} and b value is {b} and cvalue is {c}'.format(a=10,b=20,c=39)
print(v)
```
Output:
```
a value is 10 and b value is 20 and cvalue is 39
```


###  2.Type Conversion
- Type conversion int to float

The following example showing the conversion of int datatype to float datatype.

Example
```python
a=10
print('a value is {0:f}'.format(a))
```
Output:
```
a value is 10.000000
```
conversion int datatype to float datatype with **2** precision point.

Example
```python
a=10
print('a value is {0:.2f}'.format(a))
```
Output:
```
a value is 10.00
```
- type conversion double to float
- while calulation in python 3 the defualt return type of calculation is **double**

Example
```python
print('2/3 answer is {}'.format(2/3))
```

Output:
```
2/3 answer is 0.6666666666666666

```
- To conversion of double daatatype to float datatpe.
Example:
```python
print('2/3 answer is {0:f}'.format(2/3))
```
Output:
```
2/3 answer is 0.666667
```

### 3.Space around the word 

- This is used for giving spacing for integer variables
```python
print('answer is {0:3d}'.format(2))
```
Output:
```
answer is   2
```

here the given element is length of 1 digit and we give space for 3 digit means only 2 digit space will displayed.


- For string we use left **chevron(<)** and right **chevron(>)** for giving space

Example:
```python
print('my name is {}'.format('abhi'))
```
Output:
```
my name is abhi
```

- To give space before name we use right chevron
```python
print('my name is {0:>8}'.format('abhi'))
```
Output:
```
my name is     abhi
```

- To give space after name we use right chevron
```python
print('my name is {0:<8} ....'.format('abhi'))
```

Output:
```
my name is abhi     ....
```
### 4.Asterisk  around the text
Example:

```python
print('{0:*^11s}'.format('rahul'))
```

Output:
```
:***rahul***
```
This will create 11 * but **rahul** string is have 5 length characters so 6 asterisk(*) will be printed at 3 left side and 3 right side.
                             
if the remaining count of asterisk is odd then half number then the asterisk printed one extra at right side because asterisk 
printing start from right side to left.
Example:
```python
print('{0:*^12s}'.format('rahul'))
```

Output:
```
***rahul****
```

### 5.String Formatting inside a loop  
Example
```python
for i in range(1,11):                           
    print('{0:5d}{1:5d}{2:5d}'.format(i,i**2,i**3))
```                                

Output:
``` 1    1    1
    2    4    8
    3    9   27
    4   16   64
    5   25  125
    6   36  216
    7   49  343
    8   64  512
    9   81  729
   10  100 1000
```
