## Docstring

### Basic Introduction Of DocString

- The docstring is similar to comment which is not run by the python interpreter.
- The docstring is used to understand the functioning of the program.
- It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out.
- If you add multiple DocString to a function then only first DocString consider as DocString others consider as normal comments

We can write docstring using triple quotes

Syntax:
```python
#using SingleQuotes
'''
this is a docstring example
'''

#using Double Quotes
"""
this is a docstring example
"""
```

Docstring can be returned inside
```
1.function
2.class
3.method
```    
There are two way to access your docstring
```
1.__doc__
2.help()
```

### 1.__doc__
Syntax:
```python
#To get function docstring
functionname.__doc__

#To access class docstring
Classname.__doc__

#To access method docstring
Classname.methodname.__doc__
```

### 2.help()
- **help()** function is used to retrive all document related to class unctions and method
Syntax:
```python
help(class,function,any object)
```

- **help()** function return
```
- class docstrings
- methods doc strings
- dictionaries 
```

### 1.Function
- After the function declaration, you can write down docstring.

Syntax:
```python
def <Functionanme>():
    '''
    Add Function 
    '''
```
Example:
```python
#Addition function
def Addition(a,b):
    '''
    this function take two integer number and return the addtion
    '''
    return a+b
a=5
b=6
result=Addition(a,b)
print("Addition of a(5) and b(6)")
print(result)
#Result:11

#To access function docstring using __doc__
dstring=Addition.__doc__
print("\nDocumentaion of Addition Class")
print(dstring)
#Result:this function take two integer number and return the addtion

#To access function docstring using help() function
dstring=help(Addition)
print("\nDocumentation using help")
print(dstring)
```
Output:
```
Addition of a(5) and b(6)
11

Documentation of Addition Class

    this function takes two integer number and returns the addition
    
Help on function Addition in module __main__:

Addition(a, b)
    this function takes two integer number and returns the addition


Documentation using help
None
```

## 2.class

Syntax:
```python
class <ClassName>:
    '''    
    add class docstring here
    '''
```


Example:
```python
class Circle():
  #Add Document About Class here
  '''
  this is simple class description 
  '''
  pass

#initialize the class object
circle1=Circle()

#Get Doc string using __doc__
dstring=Circle.__doc__
print(dstring)
#Result:this is simple class description 


#Get Doc string using help()
dstring=help(Circle)
print(dstring)
```
Output
```
#Result
Help on class Circle in module __main__:

class Circle(builtins.object)
 |  this is simple class description
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
```

## 3.Methods
Syntax:
```
class <ClassName>:
   def <MethodName>():
    '''
    add method doc string here
    '''
```

Example:
```python
class Circle():
  #Add Document About Class here
  '''
  this is simple class description 
  '''
  a=5
  def Display(self):
    '''
    This is display method print the a value on console
    '''
    print("I am a From Display Method:{}".format(Circle.a))

#initialize the class object
circle1=Circle()

#Get method Doc string using  __doc__
dstring=Circle.Display.__doc__
print(dstring)
#Result: This is display method print the a value on console


#Get method Doc string using help()
dstring=help(Circle.Display)
print(dstring)
```
Output
```
Help on function Display in module __main__:

Display(self)
    This is display method print the a value on console

None
```
