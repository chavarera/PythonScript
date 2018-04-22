#function procedure when we need to do some task then the best way to reuse our code
# so function can help
#Function or procedure syntax def functionname(variabl1,variable2..):
#        return calculation
#to define a function def keyword is used

#addition function
def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

print("Addtion is ")
print(addition(19,8)) #calling a function

print("Substraction is ")
print(substraction(19,8)) #calling substraction function

print("Multiplication is ")
print(multiply(19,8)) #calling multiplication function

x=input("Enter First Number:")
y=input("Enter Second Number:")
z=(addition(int(x),int(y))) #sending user input function
print("Your Answer")
print(z)