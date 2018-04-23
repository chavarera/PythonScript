#Create a program user can enter any number then return the addition of that number
#example user enter 1234 then addition is 1+2+3+4=10
x=input('Enter the Number:')
print(x)
length=len(x)
result=0
i=0

while(i<length):
    result=result+int(x[i])
    i=i+1

print(result)

