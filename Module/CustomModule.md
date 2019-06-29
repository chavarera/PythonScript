## Custom Module

- Custom module is any python file that contains python statement and definations,
- You can Create custom module as a normal file and place within that folder

create simple module named with **Calculation.py**
```python
def Addition(a,b):
  '''Addition() function accept two integer 
  and return Additon of two variables'''
  return a+b
  
def Multiplication(a,b):
  '''Multiplication() function accept two integer 
  and return Multiplication of two variables'''
  return a*b
  
def Substraction(a,b):
  '''Substraction() function accept two integer 
  and return Substraction of two variables'''
  return a-b
  
#variable  of Module
var1= {"name": "John"}
```


import this module in your program using
```python
import <CustomModule>  as <ObjectName>
```

To access functions of Calculation module using cal module
```python
ObjectName.<MethodName>(paramter)
```

To access variable name from module
```python
ObjectName.variableName
```

*Example*
```python
#import Calculation module
import Calculation

#get Documentation of module
print(help(Calculation))

#Call Addition function From Calculation Module
add=Calculation.Addition(5,4)
print(add)
#Result:9


#Call Multiplication Function from Calculation.py
mul=Calculation.Multiplication(4,8)
print(mul)
#Result:32


#get The variable from module
var=Calculation.var1['name']
print(var)
#Result:jhon


#list out customcuntion 
print(dir(Calculation))
'''
['Addition', 'Multiplication', 'Substraction', 
'__builtins__', '__cached__', '__doc__',
'__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'var1']

'''


'''
#Result:
Help on module Calculation:

NAME
    Calculation

FUNCTIONS
    Addition(a, b)
        Addition() function accept two integer 
        and return Additon of two variables
    
    Multiplication(a, b)
        Multiplication() function accept two integer
        and return Multiplication of two variables
    
    Substraction(a, b)
        Substraction() function accept two integer 
        and return Substraction of two variables

DATA
    var1 = {'name': 'John'}

FILE
    /tmp/sessions/e874d61211858ec0/Calculation.py


None
9
32
John
['Addition', 'Multiplication', 'Substraction',
'__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__spec__', 'var1']

'''
```
