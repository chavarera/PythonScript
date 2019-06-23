## Classes and Objects

### Basic of class and Objects

### What is mean by class
- Almost everything in Python is an object, with its properties and methods.
- The primitive data structures available in Python, like numbers, strings, and lists are designed to represent simple things.But when you need to handle complex things we required classes.
- Classes are used to create new user-defined data structures that contain arbitrary information about something. 

Consider a simple example if there are 5 person and you want to save age,name,salary normally then you need to creates lots of variable for each person.you can reduce this using classes and object . Just normal create class with age,name,salary attribute And create a class object for every person when you calling to class.

- class just provides structure—it’s a blueprint for how something should be defined.
- A class is a code template for creating objects. Objects have member variables and have behaviour associated with them.
- class contains collection of attributes and methods.


### How to define class in Python?
- In Python a class is created using **class** keyword
- Then you add the name of the class (starting with a capital letter.)

Syntax:
```python
class <class name>:
        #attributes
        #methods

#Or another way 
class <class name>():
        #attributes
        #methods
```

Example:
```python
class Person:
     #initialize the variable(attributes)
     name="python"

    #initialize the methods(functions)
     def Display(self):
            print("i am from Display method")
```
Another Example:-
```python
class Person():
     #initialize the variable(attributes)
     name="python"

    #initialize the methods(functions)
     def Display(self):
            print("i am from Display method")
```

**Note**:-if you run above programm you will not get any output because a class is useless until it's object is created.

### How to create an empty class

Example:
```python
class Person:
       pass
```

### ome standard rules to create class
- class name first character should be in capital case.
- Class name must be started with alphabets and underscore(_).
- Do not use special keyowords as class name.
- do not use special character in class name except underscore(_).
- class name can be combination of alphabets,digit, underscore but starting character should be underscore or alphabets only.
- do not use space in class name.


## Objects
### what is mean by object
- An object is an instance of a class.
- Using object we can access class attributes and methods.
- we can also modify public class attributes using object. 

## How to create an class object

After defining the class the procedure to create an object of an class

- use class name to create an object

Syntax:
```python
#Without parameter
objectname=classname()

#With Parameter
objectname=classname(parameter list)
```


Example:
```python
#initilize the class
class Person:
   #initialize the variable(attributes)
     name="python"

    #initialize the methods(functions)
     def Display(self):
            print("i am from Display method")

#initialize the class objects
p1=Person()

#create another class object
p2=Person()

#create third class object
p3=Person()
```
