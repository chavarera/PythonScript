#we alredy know how to handle error
#in this example we using while loop to take correct input from user
#the while loop runs untill user enter both correct number

x=input('Enter First Number: ')
y=input('Enter Second Number: ')

while True:
    try:
        if int(x)>int(y):
            print(str(x)+' is greator number')
        else:
            print(str(y)+' is greator number')
    except:
        print('You did not entered numeric value')
        print('try again ')
        x=input('Enter First Number: ')
        y=input('Enter Second Number: ')
        continue
    else:
        print('two number compared successfully')
        break
