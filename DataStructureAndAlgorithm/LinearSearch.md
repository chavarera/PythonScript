## Search Algorithm

```
1.Linear Search
2.Binary Search
```

### 1.Linear Search
- Linear search is also called as sequential search
- It sequentially checks each element of the list until a match is found or the whole list has been searched if element is not found.
- But linear search rearly used in practical scenario.

#### Advantages
 - When a key element matches the first element in the array then this is best case Scenario.
 - Linear Search Also Can work on unorderd list of element.

#### Disadvantages
- When a key element matches the last element in the array or a key element doesn't matches any element then Linear search algorithm is a worst case.


#### Algorithm

Consider
```
input Variable
lst   : Input List
number: Search ELement

Output Variable
result    : True if Element is Found Else False
index     : -1 if element is not found else return index of search element.
iteration : return Number of iteration 
```

**Step1** : Initialize a boolean variable result and set it to False initially , initialize index variable and set -1 initially.
```python
result=False
index=-1
```

**Step2** : Start for loop with i ranging from 0 to the length of the list

**Step3** : Check if number element is equal to lst[i] if equals
- set result boolean variable to True
- set index variable to i
- break for loop

**Step4** : Return the result,index,iteration


#### Program

```python
def LinearSearch(lst,number):
  '''Function Input
        lst: A Integer Element List
        number: The Number which Do you Want to Search
        
     Function Output:
        result: True if number is found else False
        index: if element found then index else return -1 if element is not found
        iteration : Total No of Iteration Required
  '''
  
  result=False
  iteration=0
  index=-1
  
  
  for i in range(len(lst)):
    iteration+=1
    if lst[i]==number:
      result=True
      index=i
      break
  return result,index,iteration
    

#Driver Program  
#Simple List
lst=[1,2,3,4,5,6,7,8,9,10]

# Print Normal List
print(lst)
#Get Use Input From User
number=int(input("Enter Search Number:"))

#Call Search Function and save result in res and No of iteration in iteration
res,index,iteration=LinearSearch(lst,number)

#Print the Result
print("\nNumber In List: {} \nNumber Index :{} \nIt Required iteration: {}".format(res,index,iteration))
```

Output for 2 Input:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 2

Number In List: True 
Number Index :1 
It Required iteration: 2
```

Output for 11 Input:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 11

Number In List: False 
Number Index :-1 
It Required iteration: 10
```

Output for 5 Input:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter Search Number: 5

Number In List: True 
Number Index :4 
It Required iteration: 5
```

#### Time Complexity for ordered Linear search
**1.Best Case**
- O(1)
- In above Example for element 1

**2.Average case**
- O(n)
- In above Example for element 5

**3. Worst case**
- O(n)
- In above Example for element 11

**Reason**:
 We need to go from the first element to the last so, 
 in the worst case we have to iterate through n elements, n being the size of a given array.

#### Space Complexity For ordered Linear Search
 O(1)

**Reason** :
 We don't need any extra space to store anything.We just compare the given value with the elements in an array one by one.
