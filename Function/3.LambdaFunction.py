##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:17/03/2019
#File_des:Introduction of Lambda Function
##------------------------------------------------------------------------------------------------------

'''
lambda function is a small anonymous function.
A lambda function can take any number of arguments, 
but can only have one expression.

Why Use Lambda Functions?
anonymous function is a function that is defined without a name. 
While normal functions are defined using the def keyword,

Syntax:
lambda arguments : expression


Example:
x = lambda a : a + 10
print(x(5)) 

'''
#create a lambda function which accept single elemnt and Return its Square
square=lambda num1:num1**2
print(square(2))


#Create a lambda function to accept two numbers and return addion of both Number
add=lambda a,b:a+b
print(add(5,4))

#Use Of lambda with list and Map
#multiply with each element from list with 2
#map syntax map(function,iterableobject)
li = [5, 3, 2, 7, 4, 632, 737] 
result_list = list(map(lambda x: x*2 , li)) 
print(result_list) 


#lambda function inside in a function
def Func1(n):
  return lambda a:a*n

l=Func1(4)
print(l(2))
#in above program n is 4 and a is 2 wchich passed to lambda Function
  
