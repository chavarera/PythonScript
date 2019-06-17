## Lambda Function

### Lambda Function
- A Python lambda is just a Python function.But may be like a special type of function that have limited capabilities
- Lambda function is a small anonymous function.
- lambda function can have any number of arguments but only one expression, which is evaluated and returned.
- Normally we use the **def** keyword to define a function with a name. The *lambda* keyword is used to create anonymous functions.
- Lambda functions can accept zero or morearguments but only one expression.

### Why Use Lambda Functions?

Anonymous function is a function that is defined without a name. While normal functions are defined usinig the def keyword.we don't need to write return keyword for returning the value from lambda function.


Syntax:
```python
lambda arguments : expression
```

Example:
```python
x = lambda a : a + 10
print(x(5)) 
#Result:15
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

#Result:6
```

### Is this possible to write multiline lambda
No,because lambda function is only a single line one time use function so you can not create multiline lambda function.
Lambda function can be used with python built in function such as filter(),map, list etc....


