## Indentation


### Basic of Indentation
After completion of data type and variable I hope you understand it now I am going to here to present
 *indentation* concepts which play a vital role in python app development

- One of the most distinctive features of Python is its use of indentation to mark blocks of code.
- Other some languages such as c and c++ uses curly braces({})  to differentiate block of code
- But in python we use indentation to differentiate block of code (basically tab of some active space)
- we use colon as starting of code block and after words all code block will placed.
- Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.
- A code block (body of a function, loop etc.) starts with indentation and ends with the first unindented line. 
- The amount of indentation is up to you, but it must be consistent throughout that block.

### For example:
consider if loop
In C Programing:
```python
         if(conditions) {
               #main code
        }
```
In python Programing:

```python
       if(conditions) :
               #main code
```

### How can we write code block in one line
- Indentation can be ignored in line continuation.
- But it's a good idea to always indent. It makes the code more readable.

Example:
```python
 if(conditions) :#main code
```

### If you give wrong indentation which error will occured*

Consider following code block
```python
if(conditions) :
              print("First line")
      print("second line")
```

Incorrect indentation will result into
```python
IndentationError:
```
