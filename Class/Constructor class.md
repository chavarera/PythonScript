## Constructor

### Basic Of  Constructor

- A constructor is a special type of method(function) inside a class.
- A constructor is automatically called at the time of object creation(Instantiated).
- A constructor is used to assign some memory to an instance of a class
- Constructor in python is created using the __init__ method.
- __init__() method take the first parameter as self(You can use any name but for maintaining  standard naming convention use self keyword only) 
- It's a bad idea to write your logical code inside. Because constructor block is automatically called whenever create a new object of that class.

There are two types of constructor available in python
```
- empty Constructor
- parameterized Constructor
```
### 1.Empty Constructor

Syntax:
```python
class <classname>:
    def __init__(self):
        #initilize instance variable here
```

Example:
```python
#Initilize the class
class Person:
  #initilize The class constructor
  def __init__(self):
    print("The constructor is called")


#Create an object of a Person Class
p1=Person()
```
Output:
```
Constructor is called
```

Here when we have created **p1** as class object the  __init__() constructor is automatically called.
the block of  __init__() is instantiated.

### 2.Parametrized Constructor
- To use parameterized constructor __init__() method accepts **n** no of element and you need to pass only **n-1** parameter when you are creating an object of a class
- to define an instance variable self keyword is used instance variables are called in any method using self keyword with dot(.) notation and variable name
```python
self.variablename
```

- If constructor accepting 3 elements and you passing 6 elements to the constructor. The constructor creates an exception

Syntax:
```python
#In Class
class <classname>:
    def __init__(self,paramter list):
       #initilize instance variable here
       self.parameter1=parameter1
       self.parameter2=parameter2

#Creating Objects 
objectname=<ClassName>(paramters except self)
```

Example:
```python
#Initilize the class
class Person:
    #initilize The class constructor
    def __init__(self,name,age):
        print("The constructor is called")
        #Initilize the instance Variable
        self.name=name
        self.age=age

   #Simple method for displaying output
    def Display(self):
        print('name: '+self.name)
        print('age: '+str(self.age))         

#Create an object of a Person Class and pass jhon as name and  25 as age.
p1=Person("jhon",25)

#Now to display the output call Display Method
p1.Display()
```
Output:
```
The constructor is called
name: jhon
age: 25
```
