## Instance and Class Variables
- the variable inside class also called attributes.
- there are two different types of variables appears in classes and object.
 1.instance variable
 2.class variable

## 1.instance variable
- instance variable defined inside a constructor __init__() method of the class.
- Every object has its copy of an instance
- to call an instance variable inside a class self keyword is used.
```python
self.variablename
```
- instance variables can be accessed outside of class using class object reference or class name
```python
objectname.instancevariablename
```

Syntax:
```python
class <class name>:
    def __init__(self,variable, var2):
      self.variable=variable
      self.var2=var2
```

Example:
```python
#class initilization
class Circle():
    #Define constructor with paramter
    def __init__(self,radious,pi):
        #declare instance variables here
        self.radious=radious
        self.pi=pi      #instance variable
    def area(self):
        return self.pi*self.radious**2
        
#create Object of class and pass parameter
circle1=Circle(3,3.14)  #we are sending instance variable

#Call area method using class object
print("Circle Of Area")
print(circle1.area())
```
Output:
```
Circle Of Area
28.26
```

## 2.class variable
- class variable defined outside of __init__() methods.
- Here only one copy of the class variable created and it shared with all objects of a class.
- to access class variables inside a class  we need to use class name dot(.) Notation and class variable 
classname.variable_name
- The class variable can be accessed outside of class using class name either object reference
```python
objectname.classvariable
```

Syntax:
```python
class <class name>:
  #class variables
  Var1=value

  def __init__(self,variable, var2):
         #instance variable
```

Example:
```python
#class initilization
class Circlec():
  
  #declare class variables here
  pi=3.14   
  
  #Define constructor with paramter
  def __init__(self,radious):
      self.radious=radious
  def area(self):
      #Here we called class variable in another method
      return Circlec.pi*self.radious**2 
      
#create Object of class and pass parameter
circlec=Circlec(3)

#Call area method using class object
print(circlec.area())
```
Output:
```
28.26
```
