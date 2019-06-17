## Function Arguments

### Function arguments

**What is mean by argument's**
A value passed to a function (or method) when calling the function called as arguments.

Python support following types of arguments for function

1. positional arguments
2. Default arguments
3. Keyword arguments
4. Arbitary arguments


### 1.Positional arguments

- An argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterablepreceded by * .

- In positional arguments we need to maintain sequence as we calling area.
Syntax:
```python
Functionname(element1,element2)

#Or
Functionname(*(element1,element2))
```

Example
```python
def Addition(a,b):
       return a+b
res=Addition(5,6)
print(res)

#Result:11
```


### 2.Keyword arguments
- An argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by **
- Here we don't need to maintain position because we are defining element with one keyword.


How to define keyword arguments

Syntax:
```python
Functionname(key1=value,key2=value2)

#Using Dictionary
functionname(**{'key1':value1,'key2':value2})
```

How to access elements in function
Syntax:
```
def functionname(key1,key2):
     #function code block
```
Example:
```python
def Addition(b,a):
   return a+b

#keyword using
res=Addition(a=5,b=7)

#Using keywords with dictionary
result= Addition(**{'a':5,'b':7})

print(res)
#Result:12

print(result)
#Result:12
```


### 3.Defualt parameter
- Python allows function arguments to have default values. 
- If the function is called without the argument, the argument gets its default value.

The default value is assigned by using assignment(=) operator of the

Syntax:
```python
keywordname=value.
```

Example 1:
```
def Addition(a,b=7):
      #here default of b is set to 7 if b is not passed
      return a+b

res=Addition(5) 
# here we have pass only a value
print(res)

#Result:12
```

Example 2:
```python
def Addition(a,b=7):
      #here default value 7 is not set because we have passed a,b from calling function
      return a+b

res=Addition(5,9) 
# here we have pass only a,b value
print(res)

#Result:14
```


### 4.Arbitary arguments
- In Python, we can pass a variable(dynamic length) number of arguments to a function using special symbols. 

There are two special symbols:
1. *args(Non Keyword Arguments)
2. \*\*kwargs (Keyword Arguments)

#### 1. \*args
- Python has *args which allow us to pass the variable number of non keyword arguments to function.
- Use an asterisk * before the parameter name to pass variable length arguments.
-The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as the parameter excluding asterisk *


Syntax:
```python
#When calling function
functionname(V1,V2,V3.....)


#Inside Function
def functioname(*varname):
       for i in varname:
           #do your computation on i variable
```


Example:
```python
def Addition(*numb):
   add=0
   for i in numb:
     add=add+i

   return add

#send 2 arguments
res=Addition(5,6)
print(res)
#Result:11

#send 3 arguments
res=Addition(5,6,7)
print(res)
#Result:18

#send 4 arguments
res=Addition(5,6,7,1)
print(res)
#Result:19
```
-------------------------------------------------------------

### 2.**kwargs 
- **kwargs, it allows us to pass the variable length of keyword arguments to the function.
- The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.

Syntax:
```python
#When calling function
functionname(k1=V1,k2=V2,k3=V3.....)


#Inside Function
def functioname(**varname):
       for key,value in varname.items():
           # do operation on key and value
```

Example:
```python
def Addition(**numb):
     add=0
     for key,value in numb:
           add=add+value
     return add

#send 2 arguments
res=Addition(a=5,b=6)
print(res)
#Result:11

#send 3 arguments
res=Addition(a=5,b=6,c=7)
print(res)
#Result:18
```
