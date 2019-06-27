## Abstraction


- Key concept of object oriented programming language.
- Data abstraction main goal is to hide unnecessary details from the user.
- User can not see the atcual background process (Real time example: Atm Machine).
- When we matter input and output we don't need to understand background mechanism of that process.

![Abstraction](https://github.com/chavarera/PythonScript/blob/master/Class/abstractclasses.png)


### Abstract Classes in Python*
- Abstract class can be considered as template or bluebrint for other classes, allows you to create a set of methods that must be created within child classes.
- The class which can not be instantiated (not able to create an object of that class) and contain atleast one abstract method called as abstract classes.
if you try to create an object of abstract class you will get error
```python
TypeError: Can't instantiate abstract class Calculation with abstract methods Add
```
- Abstract methods are those methods that are declared in abstract class and must be implemented in subclass(child class).


### Algorithm

1.We need to import abc module to create abstract classes
```python
from abc import ABC,abstractmethod
```
2. Create abstract base class from inheriting ABC as parent class.
```python
class <AbstractClassName>(ABC)
```
3. Now create an abstract method inside abstract class using decorator @abstractmethod before the method
```python
@abstractmethod
def Addition(self):pass
```
4.Now create child classes by extending AbstractClass
```python
class <childclassName>(AbstractClassName):
	#implement the abstarct methods here
```
5.Initilize constructor of child class
```python
def __init(self,a,b):
	self.a=a
	self.b=b
```	
6.Now implement abstarct methods in child class
```python
def Addition(self):
	print(self.a+self.b)
 ```
 
if you create an abstract method in abstract class and not implemented in child class you will get  and following error
```python
TypeError: Can't instantiate abstract class <className> with abstract methods <methodName>
```
7.Create an object of Child class 
```python
objectname=childclassName(parameter)
```
8.Now Call the implmented abstract method using child class object

Syntax
```python
objectName.MethodName()
```
Example:
```python
objectName.Addition()
```

### Example
```python
#import required built in module
from abc import ABC,abstractmethod
#Abstract Class
class Calculation(ABC):
  #Normal methods
  def Addition(self):pass

  #Abstract Method
  @abstractmethod
  def Add(self):pass

#Create child class by inheriting Calculation class
class Result(Calculation):
  def __init__(self,a,b):
    self.a=a
    self.b=b
    
  #implement abstract method here in child class
  def Add(self):
    return self.a+self.b
    

#create an child class object and pass parameters
objName=Result(5,8)

#call abstract method
res=objName.Add()
print(res)
#Result:13
```

Above Example Summary

  1. abstract class name:  **Calculation**
  2. abstract method:      **Add()**
  3. normal Method:        **Addition()**
