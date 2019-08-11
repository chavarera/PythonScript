## Polymorphism

- Like other programming language python also support polymorphism.
- Sometimes an object comes in many types or forms create a method that handles such different type of data we can call it as polymorphism
-  Python you can define a method in such a way that there are multiple ways to call it.
polymorphism can be achieved using the following two terms
```
1. Method Overloading.
2. Method Overriding.
```

## 1. Method Overloading:

- Method overloading is the ability to create multiple methods with the same name and different parameter (Or Different Type)
 within the same class.
- In the simple word, creates multiple methods that can handle different data types in the same class
    
![Method Overloading](https://github.com/chavarera/PythonScript/blob/master/Class/methodOverloading.png)

Python built-in polymorphism Example 
**len()** Function can handle different datatypes 

### Example:
```python
#Get Length of string variable
mytext="I am Learning python."
length=len(mytext)
print(length)
#Result: 21


#Get length of list
mylist=[1,2,3,4,5,6,78,9,99]
length=len(mylist)
print(length)
#Result: 9


#Get Length of tuple
mytuple=(1,2,3,4,5,6,9)
length=len(mytuple)
print(length)
#Result: 7
```
Output
```
21
9
7
```

in above example **len()** is an example of polymorphism which handelling various data types(string,list,tuple)


### Custom Method Overloading
- Python directly not support a method overloading but we can trick it to access method overloading.
- Python doesn't allow to create same name method in the same class but using default argument we can achieve method overloading in class

### Example:
```python
class Student:
  #Define method to display data
  def Display(self,name=None,age=None,salary=None):
    print("Name:{}".format(str(name)))
    print("Age:{}".format(str(age)))
    print("Salary:{}".format(str(salary)))
    
  def Addition(self,a,b):
    print(a+b)
    
#create class Object
s1=Student()

#To call Addition method
s1.Addition(6,5)
#Result:11

#if you cannot call Addition method with greator and less number of param
# s1.Addition(5) #Error:TypeError: Addition() missing 1 required 

#Call Display method Without parameter
print("----Display() without parameter---")
s1.Display()


#Call Display method with single Parameter
print("\n----Display('Jhon') with single parameter---")
s1.Display("Jhon")

#Call Display method with two Parameter
print("\n----Display('Jhon',24) with two parameter---")
s1.Display("Jhon",24)


#Call Display method with three Parameter
print("\n----Display('Jhon',24,20000) with three parameter---")
s1.Display("Jhon",24,20000)

```
Output:
```
----Display() without parameter---
Name: None
Age: None
Salary: None

----Display('Jhon') with a single parameter---
Name: Jhon
Age: None
Salary: None

----Display('Jhon',24) with two parameter---
Name:Jhon
Age:24
Salary:None

----Display('Jhon',24,20000) with three parameter---
Name:Jhon
Age:24
Salary:20000
```

## 2.Method Overriding
- Simply defined in the child class a method with the same name as a method in the parent class.
- Defining multiple methods with the same name in the child class with a same or different parameter called as method overriding

![method Overriding](https://github.com/chavarera/PythonScript/blob/master/Class/Methodoverriding.png)
## Example of simple Inheritance
```python
#parent class
class Father:
  def Display(self):
    print("from parentClass:I am Father")

#Derived class from Father (Empty class)
class Son(Father):
  pass
 

#Create object of child class    
s1=Son()

#child class Doesn't have any method
s1.Display()
#still we can access parent class methods 
#becuase son is derived class from Father

#Result:
```
Output:
```
from a parent class: I am Father
```


### Example Of Method Overriding*   
```python
#parent class
class Father:
  def Display(self):
    print("from parentClass:I am Father")

#Derived class from Father (Empty class)
class Son(Father):
  def Display(self):
    print("from child class: I am Son")
 

#Create object of child class    
s1=Son()

#child class  Display() method overrids the parent class Method
s1.Display()

#overriding method is called instead of the Parent method
#if if the method is overridden then only child class method is called
```
Output:
```
from child class: I am Son
```
