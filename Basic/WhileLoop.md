## While Loop

### Introduction

- While loops repeat as long as a certain boolean condition is met.
- The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
- Mostly while loop is used when we want to iterate a dynamically number of times repeation
- The loop iterates while the condition is true.
- When the condition becomes false, program control passes to the line immediately following the loop.
- Iteration means executing the same block of code over and over, potentially many times

Syntax:
```python
while [condition]:
           #run this code until while condtion is true
```
Example:
```python
a=10
while(a==0):
   print(a)
   a-=1
```
### Interruption of Loop Iteration
  - In each example you have seen so far, the entire body of the while loop is executed on each iteration. 
  - Python provides two keywords that terminate a loop iteration prematurely:
    1. break
    2. continue

### 1.break
- Immediately terminates a loop entirely. 
- Program execution proceeds to the first statement following the loop body.

Example:
```python
n = 5
while n > 0:
   n -= 1
   if n == 2:
      break
   print(n)
print('Loop ended.')
```
when n becomes 2 the break statement is executed.loop is terminated completely, 
and program execution jumps to the print()statement on line 7.

### 2. continue
- Immediately terminates the current loop iteration. 
- Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will execute again or terminate.

Example:
```python
n = 5
while n > 0:
     n -= 1
     if n == 2:
         continue
     print(n)
print('Loop ended.')
```
when n is 2, the continue statement causes termination of that iteration. 
Thus, 2 isn’t printed.
Execution returns to the top of the loop, the condition is re-evaluated, and it is still true.

