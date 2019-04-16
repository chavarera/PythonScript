'''
-ErrorHandling in python is similar to other programming languages
-Why we Need Error Handler in our programs#Asume that you have written a program contains methods functions and some logic you are 
taking some input from user if that user enter some unethical data then your program create error and 
all other code from error will not run
So recover from this problem we are using error handling mechanism to give user warning or 
info whats wrong in input and executes other remainng code
'''

#Error Handling uses following 4 Keywords

#1.try:try to identify error
#2.except:if try  capture any error then except block will run(here except work like catch block in other programing langueg)
#3.else:if try doesnt capture any error then else block will run
#4.finally:this block will run in both situation when the errors occurs or error not occures

#Simple Example

x=input('Enter first number:')
y=input('Enter second number:')
try:
    if(int(x)>int(y)):
        print('first number is greator')
    elif(x==y):
        print('both number are same')
    else:
        print('Second number is greator')
except:
    print('Enter numeric number')
else:
    print('Two number compared successfully')
finally:
    print('Program Excuted successfully')
