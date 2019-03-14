#-------------------------------------------------------------------
#		Adding Another key and Value TO Dictionary
#-------------------------------------------------------------------
simpledict={'name':'jhon','roll':12}


#add age =10 in simpledict
simpledict['age']=10
print(simpledict)


#adding imageurl=''
simpledict['imageurl']=''
print(simpledict)


#-------------------------------------------------------------------
#		Removing Value From Dictionary
#-------------------------------------------------------------------

#use pop method to remove items from dict

simpledict.pop('roll')
print(simpledict)


#-------------------------------------------------------------------
#		Deleting And Clearing Dictionary
#-------------------------------------------------------------------

#For Clearing the Dict (empty)
simpledict.clear()
print(simpledict)

#use del keyword to delete Dictionary
del simpledict


