## Inheritance

### Basic Of Inheritance
- Inheritance is an a mechanism in which one class acquire the properties and attributes of an another class.
- Using inheritance we can reuse the fields and methods of an another class.

In inheritance there are two terms

  1. Base class(Parent Class)
  2. subclass(Child class)

### 1.Base class.

- Also called as parent class.
- Parent or base classes create a pattern out of which child or subclasses can be based on. 
- Parent classes allow us to create child classes through inheritance without having to write the same code over again each time

### 2.Sub Class.

- Also called as child classes
- Child or subclasses are classes that will inherit from the parent class. 
- That means that each child class will be able to make use of the methods and variables of the parent class.

For inheriting parent class in subclass the parent  class name is passed to child class

Syntax:
```python
#simple parent. Class
class <ParentClassName>:
        #attributes
        #methods
        
#inheriting sub class from parent class.
class <ChildClassName>(ParentClassName,ClassName2):
      #attributes
      #initialize init methods
       def __init__(self,variables from parent class and subclass also):
                super._init_(attributes from base class)
               classname._init_(attributes from base class)

```
You can derive parent class attributes in child class there are two different ways 

  1. Using super keyword
  2. Using Class Name

### 1. Using super
Syntax:
```python
super()._init_(Variable from parent claas)
```
Example:
```python
#Parent Class
class A:
	def _init_(self,vara):
		self.vara=vara

#Child Class Inherits Class B
class B(A):
	def _init_(self,vara,varb):
		#Initilize Attributebuts of parent Class using super
		super()._init_(vara)
		self.varb=varb

	def Display(self):
		#print value from class A and Class B
		print(self.vara,self.varb)

#Create object of child class
b1=B(2,4)

#call method
b1.Display()

#Result:2 4
```



### 2.Using class name

Syntax:
```python
Classname._init_(self,Variable from parent claas)
```

Example
```python
#Parent Class
class A:
	def _init_(self,vara):
		self.vara=vara

#Child Class Inherits Class B
class B(A):
	def _init_(self,vara,varb):
		#Initilize Attributebuts of parent Class using classname
		A._init_(self,vara)
		self.varb=varb

	def Display(self):
		#print value from class A and Class B
		print(self.vara,self.varb)

#Create object of child class
b1=B(2,4)

#Call Methods
b1.Display()

#Result:2 4
```
           
### Types of Inheritance

 1. Single Inheritance
 
 	![Single inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/singleinheritance.png)
	
 2. Multiple Inheritance
 	![Multiple Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/multipleinheritance.png)
	
 3. Multilevel Inheritance
 	![Multilevel Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/multilevelinheritance.png)
	
 4. Hybrid Inheritance
	![Hybrid Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/hybridinheritance.png)
