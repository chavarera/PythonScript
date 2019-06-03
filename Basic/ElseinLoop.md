## Else in Loop

### Basic:
- In most of the programming languages (C/C++, Java, etc), the use of else statement has been restricted with the if conditional statements. 
But Python also allows us to use the else condition with for loops.
- Such type of else is useful only if there is an if condition present inside the loop which somehow depends on the loop variable.

### What is use of else in loop
- The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

Here else block will be executed because for loop doesn't contain any **break**  statement
```python
for i in range(1, 4):
    print(i)
else:
    print("this will be executed")
```

Here else block will not executed because for loop contains **break** statement
```python
for i in range(1, 4):
    print(i)
    break
else:
    print("this will not executed")
```

#### Note:
if for loop contain a if statement and if statement contain break. 
Consider that if statement not executed this time else block of for loop will executed


### Explain in details with example
E.g. if 5 exists in any string, if yes print accordingly.

Code:
```python
strings="HELLO"
for i in strings:
    if i== '5':
        print("5 found")
        break
else:
       print("5 not found")
#result is 5 not found
```
