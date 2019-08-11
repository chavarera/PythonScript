## Encapsulation

### Introduction

- Encapsulation is the most important principle of object-oriented programing language.
- We already know the methods and Variables you can restrict access to method and variables.
- Prevent the variable and methods from being modified using an object is known as Encapsulation.
- Encapsulation means that the internal representation of an object is generally hidden from view outside of the object’s definition.
- We can Achieve encapsulation in python by creating private attributes and methods in a class.
- unlike other programming languages public, private, protected keywords are not supported in python But this scenario can be achieved using following different access specifiers.
In python, there are three different access specifiers
```
1. public(Default)
2. private(__)
3. protected(_)
```
private (__ double underscore)  is used to Achieve Encapsulation but we need to know others also

## 1.public

- By default in a class, all variables and methods are public.
- This means they can be accessed by the class members and by the module where they imported.

### Syntax:

**Defining the class attributes and Methods**
```python
#Class variables
variablename=value

#instance variable
self.variablename=value

#methods
def MethodName():
    #code of methods
```

**Accessing public members**
```python
#Class variables
objectname.classvariable

#instance variable
objectname.instancevariables

#methods
objectname.MethodName()
```

Example
```python
class A:
    #add public class variable
    a=10
    def __init__(self,b):
        #public instance variables
        self.b=b
    def Display(self):
        print("i am a public method")
#Object of class A
a1=A(20)

#Access Class Variable 
print("Class Variable value a:"+str(a1.a))

#Modify class variables and print it
a1.a=30

print("Class Variable value after modified a:"+str(a1.a))

#Access instnace variable
print("Instance variable b: "+str(a1.b))

#Modify instancevariables and print it
a1.b=50
print("Instance Variable value after modified b:"+str(a1.b))

#Call public methods
a1.Display()
```
Output
```
Class Variable value a:10
Class Variable value after modified a:30
Instance variable b: 20
Instance Variable value after modified b:50
i am a public method
```

## 2.private:
- **__**(double underscore or dunder) is used to define private attributes in class.
- For the private attribute of a class, the name should be started with (__)
- Once you are done you can not access the variable directly from its objects.
- You can not change the value directly. 

Syntax:
**Declaring the class attributes and Methods**
```python
#for class  attributes
__attributesname=value

#For Instance Variable
self.__variablename=value

#for method
def __methodname():
    #Code of methods
```

**Accessing the class attributes outside of the class**
```python
#normal way to Access variables
objectname.variablename

#To Access Private Class Variables
objectname._classname__variablename

#To Access Private instance Variables
objectname._classname__instancevariablename

#To Access Private methods
objectname._classname__MethodName
```

Example:
```python
#class initilize
class Student:
  #private class variable
  __nameclass="java"
  def __init__(self):
    #private instance variable
    self.__name="python"

  def __Display(self):
    print("I am from private display method",self.__name)

#Create object of a class
s1=Student()

#You can Not Access private Variable direct using class object you will get error
#Remove comment of next line to check error
#print(s1.__nameclass) 
#You will get Error:'Student' object has no attribute '__nameclass'


#Access private class variables
print(s1._Student__nameclass)
#Result:java


#modify value of private nameclass class variable
s1._Student__nameclass="Modified Value"


#Access private instance  variables
print(s1._Student__name)
#Result:Python


#modify instance variable
s1._Student__name="updated Value"


#To call a private method 
s1._Student__Display()
#Result: I am from a private display method updated Value
```
Output
```
java
python
I am from a private display method updated Value
```


## 3.Protected
- To achieve protected access specifiers Add _(single underscore)  at the start of the variable name doesn't change with functionality.
- The variable can still be accessed outside of the class using the class object.
- Its value remains the same that is defined inside of the class and not overridden by another variable in the next module with the same name.
- The members declared as Protected are accessible from outside the class but only in a class derived from it that is in the child or subclass.

Syntax:
**Declaring the class attributes and Methods**
```python
#for class  attributes
_attributesname=value

#For Instance Variable
self._variablename=value

#for method
def _methodname():
    #Code of methods
```

**Accessing public members**
```python
#Class variables
objectname._classvariable

#instance variable
objectname._instancevariables

#methods
objectname._MethodName()
```

Example:
```python
# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name   # protected attribute 
        self._sal = sal     # protected attribute
class Hr(Employee):
    def __init__(self,name,salary,age):
      Employee.__init__(self,name,salary)
    def Display(self):
      print(self._name)
class Admin(Hr):
  def __init__(self,name,salary,age):
    Hr.__init__(self,name,salary,age)
  def Displays(self):
      print(self._name)
emp=Admin("Jhon",20000,20)
print(emp.Displays())
```
Output:
```
Jhon
None
```
