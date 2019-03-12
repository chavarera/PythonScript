##------------------------------------------------------------------------------------------------------
#
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:24/12/18
#File_des:Condtional Indexing and some advanced Selection
#Offical Documentation:
##------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
from numpy.random import randn


##---------------------------------------------------------------------------------------------------------------------------------
#                   Selection And Indexing In pandas dataframe
##---------------------------------------------------------------------------------------------------------------------------------

#Create Data Frame using Random int numbers
    mat=randn(6,5) #6*5 matrix of random number
    rows=['A','B','C','D','E','F'] #index
    coloumns=['V','W','X','Y','Z'] #coloumns
    df=pd.DataFrame(mat,rows,coloumns)



#To Apply Conditional Selection on whole dataframe Entire DataFrame
#object dataframe>0 will find out all element from dataframe if his value is greator than 0
print("Simple Condtional Selection  df>0 \n",df>0) #but this will give only df with true or false value just pass such condition to df t get actual result

#THis will give you dataframe object with value greator than 0 and if value is less than zero or missing df will return NaN instead of blank
print("\n\nSimple Condtional Selection  df[df>2] \n",df[df>0])


#To Apply Condtional selection on the coloumns
#Find out rows if B coloumn value is less than 0

print(df['W']<0) #this will return true or false value
print(df[df['W']<0]) #this will return entrie data frame if w COloumn element is not less than 0


#For Multiple Conditions use & to add more condtions
#print dataframe if w coloumns elements are less than 0 and y coloumns with greator than 1

dataf=df[(df['W']<0) & (df['Y']>0)] #Python by defualt and,or conditional not working use & for and ,| for or operation

print(dataf)


##---------------------------------------------------------------------------------------------------------------------------------
#                   Set And Reset Index Of data frame
##---------------------------------------------------------------------------------------------------------------------------------


#To reseting the Index
print(df.reset_index())  #This Will temporary removes the added index and give by defualt index 
#this will reset an inde to an coloumn and you will get numeric index


#To settting new index
new_index=['ab','bc','cd','ef','gh','hi']
df['new_index']=new_index # this will added a new coloumn name with new_index now you can set it as index
df.set_index("new_index")
df.set_index("new_index") # this will temporary add the new index to add permanant index use inplace=True
print(df.set_index("new_index"))

