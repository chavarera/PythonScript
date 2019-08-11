## Hybrid Inheritance

![Hybrid Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/hybridinheritance.png)

### Hybrid Inheritance
- when more than one inheritance is combined to achieve inheritance then it is called as Hybrid Inheritance


### Skelton Example of Hybrid Inheritance
```python
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
```

### Example 1
```python
class A:
  def __init__(self):
    print("Class A Is Initialized")
    self.Avar="I am A Class variable"
class B(A):
  def __init__(self):
    A.__init__(self)
    self.Bvar="I am B Class variable"
    print("From Class B "+self.Avar)
    
class C(A):
  def __init__(self):
    print("Class C Is Initialized")
    A.__init__(self)
    print("From Class C "+self.Avar)
   
    self.Cvar="I am C Class variable"
    
class D(B, C):
  def __init__(self):
    B.__init__(self)
    C.__init__(self)
    print("From Class D ")
    print(self.Avar)
    print(self.Bvar)
    print(self.Cvar)
d1=D()
```
Output:
```
Class A Is Initialized
From Class B I am A Class variable
Class C Is Initialized
Class A Is Initialized
From Class C I am A Class variable
From Class D 
I am A Class variable
I am B Class variable
I am C Class variable
```
