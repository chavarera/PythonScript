## Multilevel Inheritance

### Introduction

- The features of all the base classes are inherited into the derived class We can inherit a derived class from another derived class, this process is known as multilevel inheritance.
- This is an example of child and grand child relationship.
- Multi-level inheritance is archived when a derived class inherits another derived class. 
- There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
- when we call a method using derived class and if thta method is not avialable in that derived class it will chek it in its parent class. if that methods is not present in parent class then it will search it from grand parent.


### Algorithm

1.Create a Parent Class A.
```python
class A:
```
2.Create Class B and inherit it from class A
```python
class B(A):
```
3.Create Class C and inherit from class B
```python
class C(B):
```
4.Repeat this process untill you Required
5.Create object of last derived class and access methods and attributes of all above parent and grand parent class.

### Syntax
```python
#Parent Class For B
class <A>:
	#initilize attributes and methods
#Child Class for Class A And Parent class For Class C
class <B>(A):
	#initilize class b cand call constructor of class A

#Child class for B
class <C>(B):
	#call the constructor of class B
	#Access here Allthe properties of class A and Class B

#Create objec of C Class
c1=C()
```

### Example 1
```python
class A:
  def __init__(self):
    self.Avar="I am A Class variable"
class B(A):
  def __init__(self):
    A.__init__(self)
    self.Bvar="I am B Class variable"
class C(B):
  def __init__(self):
    B.__init__(self)
    print(self.Avar)
b1=C()

#Result:I am A Class variable
```

### Example 2
```python
#Parent Class A
class A:
  def __init__(self):
    self.Avar="I am A Class variable"
    self.a=10

#Child class B
class B(A):
  def __init__(self):
    #Call the parent class A Constructor
    A.__init__(self)
    
    #initilize Instance variables for B class
    self.Bvar="I am B Class variable"
    self.a=20
    
class C(B):
  def __init__(self):
    #Call the parent class B Constructor
    B.__init__(self)
    
    print('---------------------In Class C----------------------------')
    
    #Read Variable from class A
    print("--------------Class A variable--------------\n")
    print(self.Avar)
  
    print("\n--------------Class B variable--------------\n")
    #Read Variable From Class B
    print(self.Bvar)
    
    print('\n---------The variable from first parent class---------\n')
    #Print a value
    print(self.a)

#create object of C class
b1=C()

'''
#Result
---------------------In Class C----------------------------
--------------Class A variable--------------

I am A Class variable

--------------Class B variable--------------

I am B Class variable

---------The variable from first parent class---------

20
'''
```
