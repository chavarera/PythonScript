# For Simple example this will print series of 5 starting from 5 and end at 50 with difference 5 and addition of output numbers
# for x in range(5,50,5):
#    print(x)

def series(start, stop, step):
    result = 0
    for x in range(start, stop + 1, step):
        print(x)
        result = result + x
    print("The Addition of " + str(start) + " series is  " + str(result))


start = int(input("Enter Starting number:"))
step = int(input("Enter difference:"))
terms = int(input("Enter number of terms:"))

# to find out last number using terms number
stop = start + (terms - 1) * step

series(start, stop, step)
