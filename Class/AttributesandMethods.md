## Attributes and Methods


## Atributes
- variable inside a class are called attributes.
- A class attribute is a Python variable that belongs to a class rather than a particular object.
- It is shared between all the object of the class.
- Atrributes are defined outside the constructor methods.

Syntax:
```python
class <ClassName>:
	variablename=value
```
Example:
```python
class Person:
	#Initialize Attributes
	name="python"
	age=25
```
### How to get values of Class attribute using class objects?

- for accessing class attributes use classname and dot(.) notation 

Syntax:
```python
classobject.variablename(attributename)
```

Example:
```python
#Initilize class 
class Person:
	#Initialize Attributes
	name="python"
	age=25

#initialize the class object
p1=Person()

#To Access name Attributes
name=p1.name
print(name)
#Result:python

#To Access age Attributes
age=p1.age
print(age)
#Result:25
```

### Modify Class Attributes using Class object
- To modify class attributes use normal assignment(=) operator with class object and attributes name

Syntax:
```python
classobject.attributename=Value
```

Example:
```python
#Initilize class 
class Person:
	#Initialize Attributes
	name="python"
	age=25

#initialize the class object
p1=Person()

#Name Attribute Value Before Modification
name=p1.name
print(name)
#Result:python

#Modify name value "python" to "python 3.7"
p1.name="python 3.7"

#Now just get the value of name Attribute
name=p1.name
print(name)
#Result:python 3.7
```



## Methods
- A function inside a class is called method.
- Method are accessible within the class.
- Methods can accepts n number of parameter and return value using return keyword.

### How to define method?
- **def** keyword is used to define method.
- First parameter of method is **self**.
- In method attributes are called with Classname dot(.)notation

Syntax:
```python
Class <ClassName>:
	def MethodName(self,Paramter1,paramter2):
		#Code inside a method
```

Example:
```python
#initialize the class
class Person:
	#initialize the Method
	def Display(self):
		print(Person.name)
```

### How to call method from a class using object?

- to call a method from a class using class object we use dot(**.**) Notation

Syntax:
```python
classobject.methodname()
```

Example:
```python
#initilize the class
class Person:
   #initialize the methods
   def Display(self):
          print("simple output from Display method")

#initialize the class objects
p1=Person()

#call Display method from Person class using p1 class object
p1.Display()

#Result:simple output from Display method
```
