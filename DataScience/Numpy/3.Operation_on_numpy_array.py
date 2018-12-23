'''
Created By:Ravishankar Chavare
version:Python Version 3.7
'''

import numpy as np

first_array=np.arange(0,5)

print("First Array: ",first_array)


#Addition operation on array

addtion_array=first_array+first_array

print("Addition of two numpy array",addtion_array)


#Perform a Scalar operation means add 100 in each element of test_array
test_array=np.arange(0,10)
scalar_array=test_array+100
print("Scalar array Operation(add 100 to each array element) : ",scalar_array)


#when 0/0 in normal python it will shows error but in numpy array operation it will give nan value and a single warning

print(first_array/first_array)

#when ement/0 it will give infinity
print(first_array/0)


#square of first arry

print("Square of First Array: ",first_array**2)


#To print square root of first_arra element
print('Square root of first array:',np.sqrt(first_array))


#To get Expontial of array element
print(np.exp(first_array))


#To Find out max elemnt from array

print("Max element from first Array: ",np.max(first_array))

#to find min
print("min element from first Array: ",np.min(first_array))


#To find Out log or sin values of elemenyt
print("Sin values of first Array: ",np.sin(first_array))
