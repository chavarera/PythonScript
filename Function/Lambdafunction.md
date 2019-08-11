## Lambda Function

### Lambda Function
- A Python lambda is just a Python function. It is a simple  special type of function that has limited capabilities
- Lambda function is a small anonymous function.
- lambda function can have any number of arguments but only one expression, which is evaluated and returned.
- Normally we use the **def** keyword to define a function with a name. The *lambda* keyword is used to create anonymous functions.
- Lambda functions can accept zero or more arguments but only one expression.

### Why Use Lambda Functions?

The anonymous function is a function that is defined without a name. While normal functions are defined using the def keyword. we don't need to write a return keyword for returning the value from the lambda function.


Syntax:
```python
lambda arguments: expression
```

Example:
```python
x = lambda a : a + 10
print(x(5)) 
```
Output:
```
15
```

### Lambda function with multiple arguments

if you want to define a lambda function that accepts more than one argument, you can separate the input arguments by commas.

Syntax:
```python
lambda var1,var2,var3: computation of input variable
```
Example:
Create a lambda function for addition of two input integer number
```python
add=lambda a,b:a+b

#pass 2 and 4 number
res=add(2,4)
print(res)
```

Output:
```
6
```

### Is this possible to write multiline lambda Function
No, because lambda function is only a single line one time use function so you can not create a multiline lambda function.
Lambda function can be used with python built-in function such as filter(), map, list, etc....


