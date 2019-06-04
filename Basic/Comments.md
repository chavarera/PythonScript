## Comments :thought_balloon:

### Basic of Comments :bell:
 
- Comments :thought_balloon: are very important while writing a program.
- It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out.

For comments there are two options

#### 1.Single line comment :skull:
   - we use the hash (**#**) symbol to start writing a comment.
   - Python Interpreter ignores comment.

 For example:
 ```python
     #this is first comment
     #this is second comment
     a=5    #code with comment
```

#### 2.Multi line comment :dolls:
  - Use triple quotes, either **'''** or **"""**. For multicommenting.
  - These triple quotes are generally used for multi-line strings. 
  But they can be used as multi-line comment as well. Unless they are not docstrings, 
  they do not generate any extra code.

For Example:
```python
  ''' this is multi line comment
    Second line comment
   Third line comment
  Fourth line '''
```

Or
```python
  """this is multi line comment
    Second line comment
   Third line comment
  Fourth line """
```


### Is this possible to assign multiple lines :page_with_curl: to a single variable

yes you can use in following ways:
```python
myvar= """this is multi line comment
    Second line comment
   Third line comment
  Fourth line """
  
#for print result
print(myvar)
```

**Note:-** multi line comments are also used to create doc string for function or class
