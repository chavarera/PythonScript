## Binary Search

#### Introduction

- Binary search also known as **Half-Interval Search** or **logarithmic search** .
- Binary search is used to find the target value within a sorted array.

#### Simple Steps:
- Binary search compares the target value to the middle element of the array. 
- If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, 
- again taking the middle element to compare to the target value,and repeating this until the target value is found. 
- If the search ends with the remaining half being empty, the target is not in the array.


#### Advantages
- Binary search is faster than linear search except for small arrays.
- The algorithm is faster compared to linear search.


#### Disadvantages
- array must be sorted first to be able to apply binary search.
- binary search is Slower than hash tables.
- The worst case and the best case are nearly same for the binary search

#### Algorithm
Consider Variables
```
input Variable
lst   : Input List(sorted list)
number: Search ELement

Output Variable
result        : True if Element is Found Else False
middle(index) : -1 if element is not found else return index of search element.
iteration     : return Number of iteration 
```
**step 1** : set start variable to 0 and end variable to (length(lst)-1)
```python
start=0
end=length(lst)-1
```

**step 2** : if start is greater than end break the algorithm

**step 3** : calculate middle variable 
```python
middle=(start+end)//2
```

**step 4** : Check Following Conditions:

1. number==lst[middle] 
    - If the targe number is equal to list[middle] then search is complete .
    - Break the loop

2. number>lst[middle]
    - set the start to middle+1
      ```python
      start=middle+1
      ```
    - Got to Step 2 and repeat

3. number<lst[middle]
    - set the end to middle-1
      ```python
      end=middle-1
      ```
    - Got to Step 2 and repeat

#### Program:
```python
def BinarySearch(lst,number):
  '''Function Input
        lst: A Integer Element List
        number: The Number which Do you Want to Search
        
     Function Output:
        result: True if number is found else False
        middle(index): if element found then index else return -1 if element is not found
        iteration : Total No of Iteration Required
  '''
  
  result=False
  iteration=0
  length=len(lst)
  
  start=0
  end=length-1

  while start<=end:
    iteration+=1
    middle=(start+end)//2
    if lst[middle]==number:
      result=True
      break
    
    elif number>lst[middle]:
        start=middle+1
    elif number <lst[middle]:
        end=middle-1
  else:
      middle=-1
      
  return result,middle,iteration
  
#Driver Program  
#Simple List
lst=[1,2,3,4,5,6,7,8,9,10]

# Print Normal List
print(lst)
#Get Use Input From User
number=int(input("Enter Search Number:"))

#Call Search Function and save result in res and No of iteration in iteration
res,index,iteration=BinarySearch(lst,number)

#Print the Result
print("\nNumber In List: {} \nNumber Index :{} \nRequired iteration: {}".format(res,index,iteration))
		
```

Output for 2 Input
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 2

Number In List: True 
Number Index :1 
Required iteration: 2
```

Output For 11 Input
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 11

Number In List: False 
Number Index :-1 
Required iteration: 4
```

Output for 5 input
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 5

Number In List: True 
Number Index :4 
Required iteration: 1
```

#### Time Complexity
- Best Case O(1)
- Average Case O(log n)
- Worst Case O(log n)

#### Space Complexity
O(1)
