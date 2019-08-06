## Variable And Data Types

### Variable 

- A variable can be thought of as a memory location that can hold values of a specific type.
- The value in a variable may change during the life of the program—hence the name **“variable”**.
- In c programming or other some programing while defining variable we need to assign its data type but in python, we don’t need to write data type before the variable

Syntax to write variable
```python
Variablename=value
```
Example for an integer variable 
```python
#In C Program
int a=2;
#In Python Program
a=2 
```
here we don’t need to write int as data type

Example of character variable definition
```python
#In c Program
char var=’A’;

#In Python Program
var=’A’
```

### Following are some example to define a variable in python
```python
#String variable definition
myvar="this is simple string"

#Float variable
Myvar=5.5

#List variable
mylist=[1,3,5]

#Tuple variable
mytuple=(7,5,8,5,’c’)

#dictionary variable
mydct={’keyname’:’value’}

#set variable
myset={2, 4,7}
```


### How to define multiple variables in a single line
if we want to assign a=5, b=6, c=7
```python
a, b, c=5,6,7
```

Use comma **(,)**  delamination to specify multiple variable in a single line

**Note:** both side count should be same otherwise it will raise an error

### How to assign the same value to multiple variables. 
```python
a=b=c=3

#here if you print result

print(a) #3
print(b) #3
print(c) #3
```

Here all three variable a, b, c are assigned to the same memory location

### Some rules while creating variable 
- Use variable naming convention means variable name related to real-world 

example
```python
For example : person_name
Instead of :  pn
```
- Variable name must be started with alphabets or underscore not with a numeric and other characters
- You can use numbers in another position but not at first.
- The variable should not contain any space
- Do not use reserve keyword name as a variable name like list,int, str.


### How to find out the variable data type 
to find data type of already defined variable there is one default method called **type()**

Example 1
```python
a=5
print(type(a))
#This will give a result as int class
```
Example 
```python
txt="sample string"
print(type(txt))
#This will return string
```

### Find out memory location Id where the variable is saved
use python default method **Id()**

```python
a=62
print(id(a)) *#code changes here
```

This will give you int result with a memory location.



### Global variable and local variable
- Every variable has its scope depending upon variable declaration block
#### 1. Global Variable 
- Global variables are the ones that are defined and declared outside a function, and we need to use them inside a function.
- If you defined a variable outside of the function that can be accessed by other function so this is a global variable
Example
```python
#Simple Global Variable
 mytext = “I am Global Value for mytext”
def foo():  
    print(mytext)  
  
#Calling foo() function
foo() 
```

#### 2. Local Variable 
- If a variable with the same name is defined inside the scope of function as well, as it will print the value given inside the function only and not the global value.
- If a variable inside a function this is a simple example of  a local variable
- This variable is accessible only by that function where it defined
Example
```python
# Global scope can be accessible in all function 
mytext = “I am from Global variable” 
def foo():  
    #local Variable
    mytext = “I am from local variable” 
    print(mytext)

#print local value
foo()

#print global value
print(mytext)
```
