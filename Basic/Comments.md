## Indentation 


### Basic of Indentation  
**indentation** concepts which play a vital role in python app development

- One of the most distinctive features of Python is its use of indentation to mark blocks of code.
- Other some languages such as c and c++ uses curly braces(**{}**)  to differentiate block of code
- But in python, we use indentation to differentiate block of code (basically tab of some active space)
- we use a colon as the starting of code block and afterwords all code block will be placed.
- Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.
- A code block (body of a function, loop, etc.) starts with indentation and ends with the first unindented line. 
- The amount of indentation is up to you, but it must be consistent throughout that block.

### For example:
consider if loop
In C Programing :scroll:: 
```python
if(conditions) {
   #main code
}
```
In python Programing:

With  Brackets
```python
if(conditions) :
    #Write Your Main Code Here
```

without Brackets
```python
if conditions:
    #Write Your Main Code Here
```

### How can we write code block  in one line
- Indentation can be ignored in line with continuation.
- But it's a good idea to always indent. It makes the code more readable.
Example:
with Brackets
```python
if(conditions) :#main code
```

Without Brackets
```python
if conditions: #Write Your Main Code Here
```

### Wrong Spaces Inside Program Create Indentation Error.

Consider following code block
```python
if(1==1) :
              print("First line")
      print("second line")
```

Incorrect indentation will result into 
```python
IndentationError: unindent does not match any outer indentation level
```

Correct Solution
```python
if 1==1 :
  print("First line")
  print("second line")
```

Output
```
First line
second line
```
