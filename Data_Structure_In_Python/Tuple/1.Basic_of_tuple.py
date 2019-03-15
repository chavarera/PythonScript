##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:13/03/2019
#File_des:Introduction of Tuple Data Structure
##------------------------------------------------------------------------------------------------------

'''
-A tuple is a collection which is ordered and unchangeable.
-In Python tuples are written with round brackets.

'''

#Create A blank Tuple
blanktuple=() #you can also use blanktuple=tuple()
print(type(blanktuple))#Print the type of above object

#Create A tuple with 5 element
elements=(1,2,3,4,5,6,7)
print(elements) #printing the Element

#Accessing Tuple

#Accessing first element
firstelement=elements[1]
print(firstelement)


#Changing the first element
elements[1]=9 #TypeError: 'tuple' object does not support item assignment
print(elements)



