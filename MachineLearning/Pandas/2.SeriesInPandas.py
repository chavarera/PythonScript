##------------------------------------------------------------------------------------------------------
#
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:24/12/18
#File_des:Introduction of Series
#Offical Documentation:https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.Series.html
#
##------------------------------------------------------------------------------------------------------

'''
-Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
The axis labels are collectively called index
-Pandas Series can hold different variety of python data objects like list,array,dictionary,numpyarray
-Handling data objects flexibly
-Series is similar to numpy labels but the difference is that series holds values with indexing(With label)


Syantax of Series:pandas.Series( data, index, dtype, copy)

'''

import pandas as pd
import numpy as np

string_list=['a','b','c']
int_array=[100,200,300]
numpy_array=np.array(int_array)
dictionary={'b':100,'b':200,'c':300}

'''
To create panda series object
pd.Series(data=None,index=None,dtype=None,name=None,copy=False,Fastpath=False)

'''

##----------------------------------------------------------------------------------------------------------------------------------
#                                       *Create a Simple Series Object*
##----------------------------------------------------------------------------------------------------------------------------------

print('\n*******Create a Simple Series Object******')
#Create Empty series
empty_series=pd.Series()
print("Empty Series: ",empty_series)


#Create Simple Series Using List
simple_series=pd.Series(data=int_array)
print('Simple Series Object Created using array\n',simple_series) #Here 100,200,300 are datapoint placed with index 0,1,2 accordingly


#You can change the index values in series
series_with_labels=pd.Series(data=int_array,index=string_list) #another simple way pd.series(dataname,label name)
another_series=pd.Series(int_array,string_list) #do in same order firs data then labels
print('Simple Series Object Created using array with labels \n',series_with_labels)

#Create Series Object using numpy array
numpy_arr=np.arange(1,10)
numpy_series=pd.Series(numpy_arr)
print("Simple Series using numpy object :\n",numpy_series)



#Create Series Object using dictionary
series_dict=pd.Series(dictionary) #This will simple use key as index or label and value as data point
print('Simple Series Object Created using dictionary \n',series_with_labels)


#Create a Series object from scalar
scalar=pd.Series(5,index=[0,1,2,3,4])
print("Series Using Scalar :\n",scalar)


#You Can pass some built in functions to series it will hold that build in functions
buil_function=pd.Series(data=[print,list,str,int,sum])
print('Simple Series Object Created using buil_function \n',buil_function)


##----------------------------------------------------------------------------------------------------------------------------------
#                                   *Accessing The Datapoint from a series*
##----------------------------------------------------------------------------------------------------------------------------------

print('\n********Accessing The Datapoint from a series*******')
'''
-You can Access ELement from series simlar as dictionary using index it can be string or number
-you can access element using label if a label is not contained then an exception is occured 
'''
simple_series=pd.Series([10,50,70,68,14],['a','b','c','d','e'])

#To Access First Element From Series
print("First Element From Series",simple_series[0])

# To Retrive first 2 element
print("First two Element From Series\n",simple_series[:2])


#To Retrive data using labels(Retrive 14)
print("simple_series['e'] :",simple_series['e'])


#Retrive multiple element from a series
mul_element=simple_series[['a','d','b']]
print("Retriving multiple elment \n",mul_element)

##----------------------------------------------------------------------------------------------------------------------------------
#                                   *Simple Addition Operation on Series*
##----------------------------------------------------------------------------------------------------------------------------------

print('\n*********Simple Addition on Series********')

series1=pd.Series([10,50,70,68,14],['a','b','c','d','e'])
series2=pd.Series([10,50,70,14],['a','c','d','e'])

#Addition of two series objectinto result
result=series1+series2

print(result)   #it will generate a NaN if missing index found

##a     20.0
##b      NaN  b index is not found in series2 so its datapoint value to be NaN A missing value
##c    120.0
##d    138.0
##e     28.0
##dtype: float64
