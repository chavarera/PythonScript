'''
Set
-A set is a collection which is unordered and unindexed. 
-In Python sets are written with curly brackets.

simple syntax
  myset={'value1','value2'}
  or
  myset=set() #for blank set

'''
#Create a Simple set with three elements
simpleset={'first','second','third'}

#TO get item from set
'''
Set doesnt contain index value becuase it is unordered list 
we can use loop to get item from set or use 'in' to get elements
'''
#print the set
for i in simpleset:
  print(i)
  
#Chek item in set
checkitem="first" in simpleset
print(checkitem)

#To get length of set
length=len(simpleset)
print(length)

