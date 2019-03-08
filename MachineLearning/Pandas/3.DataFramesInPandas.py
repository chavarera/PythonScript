##------------------------------------------------------------------------------------------------------
#
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:24/12/18
#File_des:Introduction of DataFrames
#Offical Documentation:https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.html
#
##------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
from numpy.random import randn

'''
DataFrame:-
    -DataFrame Is Bunch of series that share the same index.
    -A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

A pandas DataFrame can be created using the following constructor −
    pd.DataFrame( data, index, columns, dtype, copy)

DataFrame Can be Created using list,dict,series,numpy ndarrays,another dataframe

'''

##------------------------------------------------------------------------------------------------------------------
#                                       *DataFrame Creatation*
##------------------------------------------------------------------------------------------------------------------

#Create an Empty DataFrame
edf = pd.DataFrame()
print("Empty DataFrame \n",edf)


#Create DataFrame Using Dictionary
my_dict={'coloumn1':[1,2,3,4],'coloumn2':[5,6,7,8]}
df=pd.DataFrame(data=my_dict,index=['a','b','c','d'])
print("Simple DataFrame using dictionary \n",df)


#Create Data Frame using Random int numbers
mat=randn(6,5) #6*5 matrix of random number
rows=['A','B','C','D','E','F'] #index 
coloumns=['V','W','X','Y','Z'] #coloumns
ndf=pd.DataFrame(mat,rows,coloumns)
print("Simple DataFrame using Random  \n",ndf)


#Data frame using matrix
mdf=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],['A','B','C'],['X','Y','Z'])
print("DataFrame using matrix  \n",mdf)




##------------------------------------------------------------------------------------------------------------------
#                           *DataFrame Selection And Indexing*
##------------------------------------------------------------------------------------------------------------------

simpledf=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],['A','B','C'],['X','Y','Z'])

#To Retrive X Coloumn use dataframe['coloumn name'] this will generate a pandas series
print("X Coloumn \n",simpledf['X']) #You can also use simpledf.X this will also give same result


#To Retrive multiple coloumn 
print("Multiple Coloumns \n",simpledf[['X','Z']]) #dataframename[[Array of required coloumns]]


#TO Retriving Rows or slecting rows thhere are two methods
'''
1.To use loc
dataframe.loc['Row Name']

this will return a series object similar to coloumns Selection
'''
select_firstrow=simpledf.loc['A']
print("Selecting First Row using loc['A'] \n",select_firstrow)


'''
2.to use iloc
this will fetch data using numerical index even index contains labels
    dataframe.loc[index]

this will return a series object similar to coloumns Selection
'''
rowusingindex=simpledf.iloc[1]
print("Selecting second  Row using loc[1] \n",rowusingindex)


#TO select row and coloumn at a time(Retrive 5 value)
selectfive=simpledf.loc['B','Y']    #datafrme.loc['row','coloumns']
print("Retrive single elemnt  using datafrme.loc['row','coloumns'] :",selectfive)


#TO Select multiple row and coloumns
selectdata=simpledf.loc[['A','C'],['X','Z']]
print("Retrive multiple subset :\n",selectdata)



##------------------------------------------------------------------------------------------------------------------
#                          *Modifying and aletering alredy Created dataFrame Object*
##------------------------------------------------------------------------------------------------------------------
olddf=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],['A','B','C'],['X','Y','Z'])

#To Add new Coloumn with name total
olddf['total']=olddf['X']+olddf['Y']+olddf['Z']
print(olddf)


#To Removing Coloumn use drop method
'''
1.input is coloumn name
2.axis will be 1 for coloumn and 0 for row but bydefualt is 0 when you are not giving axis value externally
3.inplace should be true to apply current chhanges permannatly(if you didnt used it then drop method just drop the coloum
for that stament only you can access main df as it is)
'''
olddf.drop('X',axis=1,inplace=True)
print(olddf)



#To Remove rows
'''

olddf.drop('rows',axis=0)
'''
olddf.drop('A',axis=0,inplace=True)
print(olddf)

