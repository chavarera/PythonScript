## Numpy Array Create

### Import Required Module Numpy and Rename 


```python
import numpy as np
```

#### Numpy Array Using List


```python
#Define Simple List
lst=[10,23,2,3,7,8]

#Create numpy array using lst
np_array=np.array(lst)

#print numpy array
print("Create Numpy Array Using List:\n",np_array)
```
Output:

    Create Numpy Array Using List:
     [10 23  2  3  7  8]
    

#### Numpy Array Using Tuple


```python
#Define Simple Tuple
tple=(10,23,2,3,7,8)

#Create numpy array using tuple
np_array=np.array(tple)

#print numpy array
print("Create a Numpy Array Using Tuple:\n",np_array)
```
Output:

    Create a Numpy Array Using Tuple:
     [10 23  2  3  7  8]
    

#### Numpy String Array


```python
tple=np.array(['P','Y','T','H','O','N'])
#Create numpy array using tuple
np_array=np.array(tple)

#print numpy array
print("Create Numpy Array Using Characters :\n",np_array)
```
Output:

    Create Numpy Array Using Characters :
     ['P' 'Y' 'T' 'H' 'O' 'N']
    

#### Create Numpy array using arange() function


```python
#Simple Array Here Only End is Specified
arr=np.arange(6)
print("Array With stop Parameter: ",arr)
print("Type of an Array: ",arr.dtype)


#Create Float Array
arr=np.arange(6.0)
print("\nArray With stop Parameter: ",arr)
print("Type of an Array: ",arr.dtype)


#Numpy Array From Specific Range
arr=np.arange(4,9) #it will include 4 and exclude 9
print("\nArray With Specified Range: ",arr)
print("Type of an Array: ",arr.dtype)


#Simple Numpy array with Step counter(print 5 table)
arr=np.arange(5,51,5)
print("\nArray of 5 Table: ",arr)
print("Type of an Array: ",arr.dtype)
```
Output:

    Array With stop Parameter:  [0 1 2 3 4 5]
    Type of an Array:  int32
    
    Array With stop Parameter:  [0. 1. 2. 3. 4. 5.]
    Type of an Array:  float64
    
    Array With Specified Range:  [4 5 6 7 8]
    Type of an Array:  int32
    
    Array of 5 Table:  [ 5 10 15 20 25 30 35 40 45 50]
    Type of an Array:  int32
    

## important Terminologies Used In Numpy array


```python
#Simple list
lst=[1,2,3]
np_ar=np.array(lst)

```

#### Print The Numpy Array


```python
# print Normal numpy array
print(np_ar)
```
Output:

    [1 2 3]
    

#### Get Shape of Numpy array
Use the following syntax to get the shape of numpy array
numpy_array.shape

```python
#This is 1d Array So Only 
shape=np_ar.shape
print("Shape Of an Array(row,columns):",shape)
```
Output:

    Shape Of an Array(row, columns): (3,)
    

#### Get  element data types in numpy array
numpy_array.dtype

```python
data_type=np_ar.dtype
print("Data Type Of Numpy Array:",data_type)
```
Output:

    Data Type Of Numpy Array: int32
    

#### Get Dimension Of Numpy Array
- To get the Dimension of numpy array simple call *ndim* with numpy array
numpy_array.ndim

```python
dim=np_ar.ndim
print("The dimension of the Numpy Array:",dim)
```
Output:

    The dimension of the Numpy Array: 1
    

#### Get Element Count(Size How many Element in numpy array)
- To simply get the Count of the present element in the numpy array use *size* as follows
numpy_array.size

```python
elem_count=np_ar.size
print("Element Count:",elem_count)
```
Output:

    Element Count: 3
    

#### Get the element  Size in Bytes


```python
size=np_ar.itemsize
print("Item Size in Bytes:",size)
```
Output:

    Item Size in Bytes: 4
    

## Type Of Numpy Array
```
1. Single Dimensional
2. Two Dimensional
3. Three Dimensional
```

### 1. Single Dimensional

![1d](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/Numpy/img/np1d.png)

```python
import numpy as np
#Simple list
lst=[1,2,3,4]

np_1d=np.array(lst)
print("1D Numpy Array:\n",np_1d)


#dimensssions
print("\nDimenssion of np_1d: ",np_1d.ndim)

#Second value from tuple is blank for shape becaue it is 1d array
print("Shape Of Array(row,colums) :",np_1d.shape)

#Get Type of Array Elements
print("Type Of Numpy Array Elements : ",np_1d.dtype)

#get Item Size 
print("Item Size: ",np_1d.itemsize)

#get objects Size 
print("Object Size: ",np_1d.size)


```
Output:

    1D Numpy Array:
     [1 2 3 4]
    
    Dimenssion of np_1d:  1
    Shape Of Array(row,colums) : (4,)
    Type Of Numpy Array Elements :  int32
    Item Size:  4
    Object Size:  4
    

### 2.Two Dimensssional
![2d](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/Numpy/img/np2d.png)


```python
import numpy as np
#2d List
lst2=[
    [1,2],
    [3,4],
    [5,6]
]

np_2d=np.array(lst2)
print("2D Numpy Array:\n",np_2d)

#dimensssions
print("\nDimenssion of np_2d: ",np_2d.ndim)

#three rows 2 columns
print("Shape Of Array(row,colums) :",np_2d.shape)

#Get Type of Array Elements
print("Type Of Numpy Array Elements : ",np_2d.dtype)

#get Item Size 
print("Size of Object Size: ",np_2d.itemsize)

#get objects Size 
print("element Count : ",np_2d.size)


```
Output:

    2D Numpy Array:
     [[1 2]
     [3 4]
     [5 6]]
    
    Dimenssion of np_2d:  2
    Shape Of Array(row,colums) : (3, 2)
    Type Of Numpy Array Elements :  int32
    Size of Object Size:  4
    element Count :  6
    

### 3. Three dimensional
![3d](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/Numpy/img/np3d.png)


```python
import numpy as np

#3d List
lst3=[
    [
        [3,4,5],
        [6,7,8],
        [9,10,11]
    ],
    [
        [0,1,2],
        [12,13,14],
        [15,16,17]
    ],
    [
        [18,19,20],
        [21,22,23],
        [24,25,27]
    ]
]

np_3d=np.array(lst3)
print(np_3d)

#dimensssions
print("\nDimenssion of np_3d: ",np_3d.ndim)

#three rows 2 columns
print("Shape Of Array(row,colums) :",np_3d.shape)

#Get Type of Array Elements
print("Type Of Numpy Array Elements : ",np_3d.dtype)

#get Item Size 
print("Size of Object Size: ",np_3d.itemsize)

#get objects Size 
print("Element Count: ",np_3d.size)
```
Output

    [[[ 3  4  5]
      [ 6  7  8]
      [ 9 10 11]]
    
     [[ 0  1  2]
      [12 13 14]
      [15 16 17]]
    
     [[18 19 20]
      [21 22 23]
      [24 25 27]]]
    
    Dimenssion of np_3d:  3
    Shape Of Array(row,colums) : (3, 3, 3)
    Type Of Numpy Array Elements :  int32
    Size of Object Size:  4
    Element Count:  27
    
