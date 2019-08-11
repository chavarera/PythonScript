## Regex

#### Introduction

- **Regex** is a short form of Regular Expression.
- a regular expression is denoted as RE (REs, regexes or regex pattern) are imported through re module.
- the regular expression in programing language is used to describing the string search pattern.
- A regular expression is a special sequence of characters that helps you match or find other strings
or sets of strings, using a specialized syntax held in a pattern.
- the regular expression could tell a program to search for specific text from the string and then to print out the result accordingly.
- Regular expression supports various things like Modifiers, Identifiers, and White space characters.

#### How To Import regular expression in python?
- **re** is a built-in module in python to perform the regular expression
```python
import re
```

Basic of re functions
```
1. findall()
2. search()
3. split()
4. sub()
```

Some Basic pattern requirements

### IDENTIFIERS:-
```
\d any number
\D anything except a number
\s space
\S anything except space
\w any character
\W anything except a character
. any character but except new line
\b white space around words
\. a period(this will find out . in the given string)
```

### MODIFIRES:-
```
{2,6} describing about numbers expecting result 2-6
+ Match 1 or More
? Match 0 or 1
* Match 0 or more
$ Match the end of string
^ Matching the begining of string
| either or (Example {1,3} | {6-9})
[] range or variance example [1-5],[A-Z]
{x} expecting "x" amount
```

### White Spaces
```
\n newline
\t tab
\e escape
\s space
\f form feed
\r return
```

**Note**: We can use a different solution for solving the same problem
