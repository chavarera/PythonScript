##---------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:13/03/2019
#File_des:Some Simple Operation on Tuple
##----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Adding Element into Tuple
#-----------------------------------------------------------------------------

#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple

tpx=(1,2,3,4,5,6,7)

#add 9
tpx=tpx+(9,)
print(tpx)

#Unlike Python lists, tuples does not have methods such as append(), remove(), extend(), insert() and pop() due to its immutable nature.



#Assigning Multiple Values
a = (1,2,3)
(one,two,three) = a
print(one)


#------------------------------------------------
#For Removing Element From Tuple
#-----------------------------------------------
#because of immutable structure we can not directly remove element from tuple here we can use list
converted_list=list(tpx)

#now we can use pop(),remove(), method to remove element
#Remove 1 from tuple
converted_list.remove(1)

#after removing element convert list to tuple

final_tuple=tuple(converted_list)


#print(tuple)
print(final_tuple)



