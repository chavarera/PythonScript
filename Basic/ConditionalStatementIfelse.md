## Conditional Statement 

### if 

Like any other programming language python also support **if-else** for the conditional statement. 

### Python supports the usual logical conditions  from mathematics 
  ```
  == :- Equals
  a == b
  
  != :- Not Equals
  a != b
  
  <  :- Less than 
  a < b
  
  <= :- Less than or equal to
  a <= b
  
  >  :- Greater than
  a > b
  
  >= :- Greater than or equal to
  a >= b
```
These conditions can be used in several ways, most commonly in **"if statements".**

Syntax:
```python
if (condition) :
    #exexute this block
```
Or without braces
```python
if condition :
   #exexute this block
```

For example
```python
a=5
if a==5:
   print("A value is 5")
```
Output:
```
 A value is 5
```

### If else 
- when we want to check one condition and if that condition met we need to execute **if** block code otherwise run **else** block

Syntax:
```python
if condition :
   #exexute this block
else:
    #execute this else block
```

For example
```python
a=5
if (a==5):
    print("A value is 5")
else:
    print("A value is not 5") 
```    

Output    :
```
A value is 5
```

Or you can simple write
```python
a=5
if a==5:
    print(" A value is 5")
else:
     print("A value is not 5")
```
Output:
```
A value is 5
```


### Nested if-else 
- There may be a situation when you want to check for another condition after a condition resolves to true. 
  In such a situation, you can use the nested if construct.

Syntax:
```PYTHON
if condition:
    #code
    if condition:
         #code here for inner if
    else:
         #else code
else:
      #outer else code add here
```

### How to use elif 
When you want to execute multiple conditions you can use **elif**

Santax:
```python
if condition:
     #add code here
elif second condition: 
     #add another code block
elif third_condition: 
     #add another code block
else:
     #add final else block
```
Here first condition check if it doesn't true then it check second condition if all **elif** conditions are fail at that time it will execute **else** block

### How to write multiple conditions in single if statement 
Use logical operator **and(&), or(|)** to checking multiple conditions

syntax
```python
if condition and condition2 and condition3:
       #code block
```

Example:
```python
a=5
b=6
c=3
large=0
if a>b and a>c :
   large=a
elif b>a and b>c :
   large=b
else:
   large=c

print(large) 
```
Output:
```
6
```
