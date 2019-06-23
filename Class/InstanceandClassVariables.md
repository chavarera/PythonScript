## Instance and Class Variables
- variable inside class also called as attributes.
- there are two different type of variables appears in classes and object.
 1.instance variable
 2.class variable

## 1.instance variable
- instance variable defined inside a constructor __init__() method of class.
- Every object has its own personal copy of an instance
- to call a instance variable inside a class self keyword is used.
```python
self.variablename
```
- instance variables can be accessed outside of class using class object reference or classname
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
        self.pi=pi      #instance variable
    def area(self):
        return self.pi*self.radious**2
        
#create Object of class and pass parameter
circle1=Circle(3,3.14)  #we are sending instance varaible

#Call area method using class object
print(circle1.area())

#Result:28.26
```

## 2.class variable
- class variable defined outside of __init__() methods.
- Here only one copy of class variable created and it shared with all object of an class.
- to access class variable inside a class  we need to use classname dot(.) Notation and class variable 
classname.variable_name
- Class variable can be accessed outside of class using class name either object reference
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

#Result :28.26
```
