## Condtional Statement :scissors:

### if :pushpin:

Like any other programming languages python also support **if else** for conditional statement. 

### Python supports the usual logical conditions  :loop: from mathematics :green_book: :
  - Equals: a == b
  - Not Equals: a != b
  - Less than: a < b
  - Less than or equal to: a <= b
  - Greater than: a > b
  - Greater than or equal to: a >= b

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
 if (a==5):
     print(" A value is 5")
```

### If else :interrobang:
- when we want check one condition and if that condition met we need to execute **if** block code other wise run **else** block

Syntax:
```python
if (condition) :
         #exexute this block
else:
       #execute this else block
```

For example
```python
 a=5
 if (a==5):
     print(" A value is 5")
 else:
     print("A value is not 5") 
```
Or you can simple write
```python
if a==5:
     print(" A value is 5")
 else:
     print("A value is not 5") 
```

### Nested if else :wavy_dash:
- There may be a situation when you want to check for another condition after a condition resolves to true. 
  In such a situation, you can use the nested if construct.

Syntax:
```PYTHON
if(condition):
    #code
    if(condition):
         #code here for inner if
     else:
         #else code
else:
      #outer else code add here
```

### How to use elif :small_red_triangle:
When you want to execute multiple condition you can use **elif**

Santax:
```python
if(condition):
     #add code here
elif(second condition): 
     #add another code block
elif(third condition): 
     #add another code block
else:
     #add final else block
```
Here first condition check if it doesn't true then it check second condition if all **elif** conditions are fail at that time it will execute **else** block

### How to write multiple condition in single if statement :o:
Use logical operator **and(&), or(|)** to checking multiple conditions

syntax
```python
if (condition) and (condition2) and (condition 3):
       #code block
```

Example:
```python
a=5
b=6
c=3
large=0
if(a>b) and (a>c) :
   large=a
elif(b>a) and (b>c) :
   large=b
else:
   large=c

print(large) 
```
