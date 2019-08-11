## Function

### Function in Python
- A function is a block of organized, reusable code that is used to perform a single, related action
- A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
- The function is a set of programmatic statements that take some input, do some specific calculation and computation
and produce expected output and return it.
- Create a function and add some commonly repeated code inside it. that instead of writing the same code again and again for different inputs, we can call the function

### How To Define a function

- Function blocks begin with the keyword **def** followed by the function name and parentheses **()**
- if Any input parameter placed with parentheses.
- The code block within every function starts with a colon **(:)** and is indented.
- for returning value from the function you can use the return keyword
```python
return "element to return"
```
- for calling the defined function we can use function-name with parentheses 

Syntax:
```python
def functionname(parameters):
    #Add main computation code here 
```
Example:
```python
def sum(a,b):
    return a+b
```

### How to Call a function
- Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt
- Call a function after the only declaration of function.if you called a function before its declaration python interpreter gives an error(name 'function' is not defined)
Example:
```python
a=5
b=7
print(sums(a,b))
def sums(a,b):
    return a+b
```
Output:
```
NameError: name 'sums' is not defined
```

The correct way to Write a function

Example:
```python
a=5
b=7
def sums(a,b):
    return a+b
print(sums(a,b))
```
Output:
```
12
```
