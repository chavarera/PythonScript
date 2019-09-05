## Numpy

![Numpy](https://numpy.org/_static/numpy_logo.png)

### Introduction
- Numpy is an abbreviated form of **Numerical Python** or **Numeric Python**.
- It is the most basic yet powerful package for scientific computing and data manipulation in Python.
- It supports large, multidimensional arrays and matrices.
- It is generally used for Data Analysis and is a part of scientific python.
- It is an extension module for Python, mostly written in C.

Official Website:https://numpy.org/

### Why Numpy?
- Numpy support N-dimensional array.
- It consumes less memory.
- NumPy array is faster than Python List
- We can create an n-dimensional array in python using numpy.array().
- Numpy array provide multidimensional slicing on an array
- Easy  for matrix computation
- In Python Array is not present where list store different types of elements but numpy helps to behave like a normal array to store similar data types.
- the list need looping to perform scalar operations

Normal List
```
lst=[1,2,3,4]
#Add 5 to every element
res=[elem+5 for elem in lst]
print(res)
#Result:
```
Output:
```
[6, 7, 8, 9]
```

Using Numpy Array
```python
import numpy as np
lst=np.array([1,2,3,4])
res=lst+5
print(res)
```
Output:
```
[6 7 8 9]
```

- Consumes Less Memory as Compared to  Python List
Python List Memory Consumes
```python
import sys
lst=list(range(0,100))
#Add 5 to every element
res=sys.getsizeof(lst)
print(res)
```
Output:
```
1008
```

Numpy Array Memory Consumes
```python
import sys
import numpy as np
lst=np.array(range(0,100))
res=sys.getsizeof(res)
print(res)
```
Output:
```
28
```


### Install Numpy Array
- Open command prompt in windows machine and type following command
```python
pip install numpy
```
- After Completion of Installation open Jupyter Notebook or python shell to test whether numpy is properly install or not.
- Type 

```python
import numpy 
```
and hit Enter if it does not give any error then your numpy is installed properly(Do not try on Normal command Prompt use python shell or any idle).


### import Numpy in Your Program
write down following line for importing Numpy
```python
import numpy
```
or Rename Numpy in Import as follows
```python
import numpy as np
```


### Create Simple Numpy Array

- To Create a simple numpy array use *array()* function.

Syntax:
```python
import numpy as np
Numpy_array=np.array(<Elements iterative>)
```

Example:
```python
import numpy as np
np_array=np.array([1,2,3,4,5])

#print Type of Array
print(type(np_array))

#print numpy array
print(np_array)
```
Output:
```
<class 'numpy.ndarray'>
[1 2 3 4 5]
```
![numpy](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/Numpy/img/numpyarray.png)
