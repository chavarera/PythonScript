#create a function who will take input as a string and search string and respond substring from string from searched string postion
def positionfinder(search,target):
    first=(search.find(target))
    second=(search.find(target,first+1))
    return second


mystring=("I like computer engineering and i am learning now")
y=(positionfinder)(mystring,"i")
print(mystring[y:])
