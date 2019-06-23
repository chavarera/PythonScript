## Constructor

### Constructor

- Constructor is an special type of method(function) inside  a class.
- Constructor are automatically Called at the time of object creation(Instantiated).
- Constructor is used to assign some memory to instance of an class
- Constructor in python is created using __init__ method.
- __init__() method take first parameter as self(You can use any name but for maintaining  standard naming convention use self keyword only) 
- Its bad idea to write your main logic inside __init__() block becuase the constructor is always called when a new object of that class is created
 alternative create a another method and write your logic ther and call it using class object

- There are two type of constructor avialable in python
    1.empty Constructor
    2.parameterized Constructor

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


#Create a object of an Person Class
p1=Person()

#Result:Constructor is called
```

Here when we have create **p1** as class object the  __init__() constructor is automaticalled called.
the block of  __init__() is instantiated.

### 2.Parametrized Constructor
- To use parametrized constructor __init__() method accepts **n** no of element and you need to pass only **n-1** paramter when you are creating object of an class
- to define instace variable self keyword is used instance variables are called in any method using self keyword with dot(.) notation and variable name
```python
self.variablename
```

- If constructor accepting 3 element and you passing 6 element to constructor.Construtor create an exception

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
```
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

#Create a object of an Person Class and pass jhon as name and  25 as age.
p1=Person("jhon",25)

#Now to display the output call Display Method
p1.Display()

'''
#Result
The constructor is called
name: jhon
age: 25
'''
```
