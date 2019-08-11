## Exception Handling

### Exception
- An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. 
- an exception is a Python object that represents an error.
- When the exceptions occur, it causes the current process to stop and passes it to the calling process until it is handled. If not handled, our program will crash.
- Error Handling in python is similar to other programming languages

### Why we Need Error Handler in our programs

Assume that you have written a program contains methods functions and some logic you are taking some input from the user 
if that user enters some unethical data then your program creates error and all other code from error will not run.
To recover from this problem we are using error handling mechanism to give user warning or info what's wrong in input and executes other remaining code.

### Why use Exception?
Exceptions are convenient in many ways for handling errors and special conditions
in a program. When you think that you have a code that can produce an error then
you can use exception handling.

The following four Keywords are used to Achieve exception handling.

#### 1. try
```
A critical operation that can raise an exception is placed inside the try block.
```
#### 2. except
```
The exception is handled in the except block which is occurred by try block.
A try clause can have any number of except clause to handle them differently 
but only one will be executed in case an exception occurs.
```
#### 3. else
```
If try block couldn't capture any exception error at that time else block is executed
```
#### 4. finally
```
Finally block is  executed  in a situation when the errors occur or error not occurs
```
Syntax:
```python
try:
    #Code block 
except:
    #Handel Exception created by try
else:
    #code when an exception is not generated
finally:
    #Executed always
```

Example 1:
```python
try:
    res=5/0
except:
    print("Not divisible by 0")
else:
    print("no error generated")
finally:
    print("Completed successfully")

```
Output:
```
Not divisible by 0
Completed successfully
```

Here **except** block and **finally**  Executed

Example 2:
```python
try:
    res=5/4
    print(res)
except:
    print("Not divisible by 0")
else:
    print("no error generated")
finally:
    print("Completed successfully")
```

Output:
```
1.25
no error generated
Completed successfully
```

here **else** and **finally** block are executed 


### How to get Exception message in except block

Syntax:
```python
except as Exception nameoferror:
    #Except for code block 
```

Example:
```python
try:
    res=5/0
    print(res)
except Exception as ex:
    print(ex)
```
Output:
```
division by zero
```

### How to Generate Custom Exception
to create a custom exception **raise** keyword is used in the try block

Syntax:
```python
try:
   raise 
except Exception as ex:
   print(ex)
```

Example:
```python
try:
    a=5
    if a==5:
        raise Exception("This is a custom exception raised using raise keyword")
except Exception as ex:
    print(ex)
```
Output:
```
This is a custom exception raised using raise keyword
```
