## Multiple Inheritance

### Introduction
- When a child class inherits from multiple parent classes, it is called as multiple inheritance.
- We specify all parent classes as comma separated list in bracket.

![Multiple Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/multipleinheritance.png)

### Algorithm

### Syntax

### Example 1
```python
class A:
  def __init__(self):
    print("Class A Is Initilized")
    self.Avar="I am A Class variable"
class B():
  def __init__(self):
    print("Class B Is Initilized")
    self.Bvar="I am B Class variable"
    
class C(B,A):
  def __init__(self):
    print("Class C Is Initilized")
    B.__init__(self)
    A.__init__(self)
   
    print(self.Bvar)
    print(self.Avar)
b1=C()
'''
#Result:
Class C Is Initilized
Class B Is Initilized
Class A Is Initilized
I am B Class variable
I am A Class variable
'''
```

### Example 2
