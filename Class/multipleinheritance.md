## Multiple Inheritance


### Introduction
- When a single **child class** inherit's from multiple parent classes, it is called as **Multiple inheritances.**
- We specify all parent Classes as a comma-separated list in child class.
- if two-parent class have the same method and you calling that method using the object of child class then the method call is dependent on which class is initialized first.

Example:
```python
def __init__(self):
    A.__init(self)
    B.__init(self)
```
here, class, A method is called First if that method not present in class A then it will execute it from class B
```python
def __init__(self):
    B.__init(self)
    A.__init(self)
```
Here class B method is called First

![Multiple Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/multipleinheritance.png)

### Algorithm
1. create a parent class
```python
class A:
```
2. Define methods and attributes
```python
def __init__(self):
    self.varsa="I am from class A"
```
3. Create an Another Parent class named B
```python
class B:
```
4. Define methods and attributes for class B
```python
def __init__(self):
    self.varsb="I am from class B
 ```
5. Now create a child class by inheriting the class A and Class B
```python
class C(A, B):
```
6. Initialize and call the constructor of class A and Class B in Construction oof class C
```python
def __init__(self):
    A.__init__(self)
    B.__init__(self)
```
7. Now you can use class A and Class B variables in Class C
```python
def __init__(self):
    A.__init__(self)
    B.__init__(self)
    #Get data of two-parent classes using self 
    print(self.varsa)
    print(self.varsb)
```
8. Then create an object of child class and call required methods and attributes using it
```python
c1=C()
```
### Example 1
```python
#Parent Class
class A:
    def __init__(self):
      self.name='Python'
      
#Parent Class
class B:
    def __init__(self):
      self.age=20
#Derive from 2 Different class
class C(B,A):
  #Constructor
  def __init__(self):
    B.__init__(self) #First B class is Initilized
    A.__init__(self)
    self.year=2019
  def ShowData(self):
    print(self.name)
    print(self.age)
    print(self.year)
c1=C()

print("Call The ShowData()")
c1.ShowData()
```
Output:
```
Call The ShowData()
Python
20
2019
```

### Example 2
```python
#Parent class 1
class A:
    def __init__(self):
      print("class A is Initialized")
      self.name='Python'

#parent class 2
class B():
    def __init__(self):
      print("Class B is Initialized")
      self.age=20

#child class C inherit from parent class 1 and parent class 2
class C(B,A):
  def __init__(self):
    print("Class C is Initialized")

    #initilize constructor B
    B.__init__(self)

    #initilize constructor A
    A.__init__(self)

    #Initilize C instance Variable
    self.year=2019

  def ShowData(self):
    print(self.name)
    print(self.age)
    print(self.year)

#Create an object of C class
c1=C()

#Call method of C Class
c1.ShowData()
```

Output
```
Class C is Initialized
Class B is Initialized
class A is Initialized
Python
20
2019
```
