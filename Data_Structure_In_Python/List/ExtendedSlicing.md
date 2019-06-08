## Extended Slicing On List

- Ever since Python 1.4, the slicing syntax has supported an optional third ``step'' or ``stride'' argument

Syntax:
```python
Listname[startindex:endindex:step]
```
Other valid syntax are

- start list from 0 index
```python
Listname[:endindex:step]
```
- Here start from 0 index and end at last element with given step
```python
Listname[::step]
 ```
- here start from startindex index and end at last element with given step
```python
Listname[startindex::step]
```

- s[i:j:k] is
"slice of s from i to j with step k".

When i and jare absent, the whole sequence is assumed and

thus **s[::k]** means "every k-th item".


Examples:

How to print 2,4,6 
```python
lists=[0,1,2,3,4,5,6,7,8,9]
start=2
end=8
step=2
result=lists[start:end:step]
print(result) 
#Result : [2,4,6]
```

- **lists[::n]** is a sequence of each **n-th** item in the entire sequence.

- [::3] just means that you have not specified any start or end indices for your slice. Since you have specified a step, 3, this will take every third entry of something starting at the first index. 
For example:
```python
lists=[0,1,2,3,4,5,6,7,8,9]
result=lists[::3]
print(result) 
#Result:[0, 6,9]
```
Let's take every 3rd item from second position list

```python
lists=[0,1,2,3,4,5,6,7,8,9]
result=lists[2::3]
print(result) 
#Result:[2,5,8]
```
