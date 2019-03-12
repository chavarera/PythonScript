'''
created By:Ravishankar Chavare
version python 3.7
How to use indexing and selection on numpy array
1.brackets
2.slicing

'''
import numpy as np

numpy_array=np.arange(1,15)
# this will create [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#to access 7 element from array use 7 as index use brackets for indexing

element_at_7th=numpy_array[7]
print('element_at_7th :',element_at_7th)


#to print element 1 to 4 need to use slicing :
#use :arrayname[startindexincluding:end index exlcuding]
slice_element=numpy_array[0:4] #or u can normally use numpy_array[:4]

print(slice_element)


#If you want to set starting 3 element value to 100

numpy_array[0:3]=100

print(numpy_array)



#if you get slice from a numpy_array and modify it actually it will also modify to main array

main_array=np.arange(20)
print("main array", main_array)

slice_of_array=main_array[0:5]

print("slice of array",slice_of_array)

slice_of_array[:]=5
print("slice of array after modification",slice_of_array)

#Here main array values also changed because slicing array refrence the array
print("main array after slice changed", main_array)



#To Solve above problem use array copy method to create the exact copy of array
num_array=np.arange(10)

copy_array=num_array[0:3].copy()
print(copy_array)

copy_array[:]=1

print("Sliced array ",copy_array)
print("num_array :",num_array)


#To Print 2d arraay
array_2d=np.array([[5,6,7],[12,10,15],[16,14,45]])

print(array_2d)

'''To accessing element from 2d array there are general two ways
1.Single bracket  Arrary_name[row,coloumn]
2.double bracket array_name[row][coloumn]

[[ 5  6  7]
 [12 10 15]
 [16 14 45]]

'''

#1To Access 10 element use following indexing method like arrayname[1][1]
print(array_2d[1][1])

#another method to acess 10 is: array[row,coloumn]

print(array_2d[1,1])



#To grabing multiple elment from array usi slicing in numpy array

#To Accessing 5,6,12,10
print(array_2d[:2,1:])


#-------------------------------------------------------------------------
#Conditional selection on numpy array

simpl_array=np.arange(2,100)

#Now find out the  elment which are less than 10 from above numpy Array

#just create a simple array to store the value
lessthan10_array=simpl_array[simpl_array<10]

print(lessthan10_array)










