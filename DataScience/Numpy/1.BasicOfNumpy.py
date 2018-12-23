'''
Created By:Raishankar Chavare
Version:python 3.7
To Install numpy

open command prompt and type:pip install numpy

To import numpy use:import numpy as np 
'''

import numpy as np
''' Simple 1 d array using numpy'''

#to create simply numpy array from a normal array use
simple_array=[1,4,2,3,5,4,5,4,5,4,8,4,58,4,8,18]

#simple 1d Array
numpy_array=np.array(simple_array)

#To Print Simple Numpy Array
print('Simple Numpy Array:' , numpy_array)


#dtype, the data type of the array
print(numpy_array.dtype)

#itemsize f the array
print(numpy_array.itemsize)

#To get the Shape of numpy array
print('1d Array Shape:' , numpy_array.shape) #The first paramter is the row and second one is empty because of 1d array

#To findout the max and min number from numpy arry use
print('Maximum Number :', numpy_array.max())#For Max
print('Minimum Number', numpy_array.min())#For Min

#To findout The Index of max number in array user argmax and for min number use argmin
print('')



#To reshaping the 1d array to multidimensssional array use reshape method
mult_array=numpy_array.reshape(4,4)

#Note Before reshaping the array check the element count neither low nor high

#print the ndimenssional aaray
print('Multidimenssional Array:\n',mult_array)


#this will print out the data into the tabular format
##[[ 1  4  2  3]
## [ 5  4  5  4]
## [ 5  4  8  4]
## [58  4  8 10]]


#shape of multidimenssional array (row,column)
print('Shape of Multidimenssional Array:',mult_array.shape)


''' numpy array operation '''

#Create a 1s array
array_1s=np.ones(5)
print('1s array',array_1s)

arrays_2s=np.ones((2,2))
print(arrays_2s)


#create numpy Array using arange function
array_using_range=np.arange(10)
print(array_using_range)


#arange with interval np.arange(start,end,interval)
arange_int=np.arange(0,20,2)
print('nparange with interval: ',arange_int)




#linspace create 10 points from 0 to 5
linspace=np.linspace(0,5,10)  #np.linspace(start,end,number of output or points)
print('10 points from 0 to 5 :\n',linspace)



#How to create 2 dimensional square matrix use np.eye(length)
square_matrix=np.eye(4) #Creating identity matrix
print(square_matrix)



#How to create numpy array using rand
#give single elemnt as parameter for 1d array and use 2 parameter for multidimenssional array
random_array=np.random.rand(4)
multi_dimenssion=np.random.rand(4,4)
print(random_array)
print(multi_dimenssion)


#To get the random integer from 1 to 100
print(np.random.randint(1,100))

#To Get the 10 random numbers from 1 to 100
print(np.random.randint(1,100,10))
