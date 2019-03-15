##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:15/03/2019
#File_des:Adding And Removing Element From Set
##------------------------------------------------------------------------------------------------------


#Simple Create a set
myset={1,2,3,4,5,6,7,8,9}
print(myset)

#NOTE:set contains unique elements
#------------------------------------------------------
#           Adding Element
#-----------------------------------------------------
'''
To adding element in set there are two way
1.add: for adding single element at a time
2.update for adding multiple element into set
'''
#add a single element to set using add method
myset.add(10)

print('After adding element10 :',myset)

#Add multiple element inside in a set
myset.update([11,12,13])
print('After multiple value Updating:',myset)

#------------------------------------------------------
#           Removing Element
#-----------------------------------------------------
'''
To remove an item in a set, use the remove(), or the discard() method.

1.remove(): If the item to remove does not exist this will raise error
2.discard(): If the item to remove does not exist this will done without raising error

you can also use pop() method to remove last element but in set there is no indexing so which elemnent at last postion is hard to tell
'''

#using remove()
myset.remove(10)
print('After removing element 10 :',myset)

#Using discard()
myset.discarrd(11)
print('After discarding element 11 :',myset)

#using pop()
myset.pop()
print('after popping  one element :',myset)

#------------------------------------------------------
#           Deleting and Clearing Set
#-----------------------------------------------------

#1.Clear the set 
myset.clear()

#2.delete the set this will completely remove the set from refrences
del myset


