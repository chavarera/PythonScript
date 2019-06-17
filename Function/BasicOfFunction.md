____________________________

Day 13:Lecture 1
Content: Function
Author:Ravishankar Chavare
Date:13-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*Function in Python*
- A function is a block of organized, reusable code that is used to perform a single, related action
- A function is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.
- Function is a set of programatic statement that take some input ,do some specific calculation and computation
and produce expected output and return it.
- Create a function and add some commonly repeated code inside it . that instead of writing the same code again and again for different inputs, we can call the function

*How To Define a function*

- Function blocks begin with the keyword *def* followed by the function name and parentheses *()*
- if Any input parameter placed with parenteses.
- The code block within every function starts with a colon (:) and is indented.
- for returning value from function you can use return keyword
return "element to return"

- for calling defined function we can use functionname with parentheses 

Syntax:
def functionname(parameters):
	#Add main computation code here 

Example:
def sum(a,b):
    return a+b

*How Call a function*
- Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt
- Call a function after only decalration of function.if you called a function beofre its declration python interpreter gives an error(name 'function' is not defined)
Example:
a=5
b=7
print(sums(a,b))
def sums(a,b):
    return a+b

#Result:name 'sums' is not defined

Correct way to Write function
Example:
a=5
b=7
def sums(a,b):
    return a+b
print(sums(a,b))
