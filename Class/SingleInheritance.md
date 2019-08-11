## Single Inheritance

### Introduction
- Only one parent class and one child class.
- When a single *child class* inherits from only one parent class it is called single inheritance.
- You can access parent and child class attributes using child class Objects.
- If parent class and child class have the same methods and you called that method using child class object then the only base class method is called.
If that method is not available in child class then the parent class method is called

![Single Inheritance](https://github.com/chavarera/PythonScript/blob/master/Class/singleinheritance.png)

### Steps to Perform Single Inheritance:

1. Create Parent (Base) class.
```python
    class A:
```
2.Define attributes and Methods in Parent Class.
```python
def __init__(self,par1,par2):
  self.par1=par1
    self.par2=par2
```

3.Create Subclass (Child) Class and Inherit it from the parent class
```python
class B(A):
```
4.Initialize the attributes and methods
5. In constructor use the super keyword to derive the parent class properties to the child class
```python
class B(A):
    def __init__(self,parameters):
            super.__init__(parameters of Parent class)
 ```
 
6. Now you can access attributes of parent class using the self keyword
```python
self.par1
```

7. Now create an object of child class and pass the required parameters
8.using base class object now you can access methods of parent and base class.

### Syntax:
```python
class <ParentClassName>:
    ##Initilize Attributes and Methods

class <ChildClassName>(ParentClassName):
    def __init__(self,ParentClass Variables,Own variables):
            super().__init__(ParentClass Variables which are Required)            
            #initilize own instance variable

#Create an object of child class
objname=ParentClassName(all paramters)

#To Call Methods of parent and child class use object of child class
objectname.methodname()
```


### Simple Example 1:
```python
#Parent Class
class A:
    def __init__(self,vara):
            self.vara=vara
#Child Class
class B(A):
    def __init__(self,vara,varb):
            super().__init__(vara)
            self.varb=varb
    def Display(self):
            #print value from class A and Class B
            print(self.vara,self.varb)
b1=B(2,4)
print("Vaue of vara and varb")
b1.Display()
```
Output:
```
Vaue of vara and varb
2 4
```

###  Simple Example 2:
```python
#Parent Class A
class A:
  def __init__(self):
    self.Avar="I am A Class variable"

#child class B
class B(A):
  def __init__(self):
    #Initilize the parent class Constructor
    super().__init__()
    
    #Get Data from class A
    print("Accessed from class B "+self.Avar)

#create object of B class
b1=B()
```
Output:
```
Accessed from class B I am A Class variable
```
    

### Example With Details:
```python
#Initilize Parent Class
class A:
    #Initilize Constructor
    def __init__(self,name):
        #initilize Instance Variables
        self.name=name

    #Initilize display() method for displaying Content
    def display(self):
        print("I am from Class A",self.name,self.age)

#Initilize Child class and Inherit it from Parent Class
class B(A):
    #Initilize Constructor
    def __init__(self,name,age):
        #Initilize derived attributes from parent Class
        super().__init__(name)

        #Initilize class B instance Variable
        self.age=age

    #Initilize display() method for displaying Content
    def display(self):
        print("I am from Class B",self.name,self.age)

#Create Object of B class
b1=B("Raj",24)

#Call the display method
print("Display Method Called")
b1.display()
```
Output:
```
Display Method Called
I am from Class B Raj 24
```

