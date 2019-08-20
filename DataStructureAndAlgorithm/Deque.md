## Deque(Double Ended Queue)

- Double-ended queue (abbreviated to **deque**) is an abstract data type that generalizes a Queue, 
for which elements can be added to or removed from either the front (head) or back (tail)
- In Normal Queue We can perform one operation at only one end. but dequeue can able to perform both insertion and removal of the item at both ends.
- Deque look similar like a queue but doesn't support FIFO structure
- Insertion and deletion of the element can be performed at both side of the queue(FRONT and REAR)

![dequeue](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/dequeue.png)

### Operations Can Be Performed
```
- Insert at Front end.
- Delete from the Front end.
- Insert at Rear end.
- Delete from Rear end.
- Check Empty dequeue
```

### Application Of Deque
- A steal Algorithm for job scheduling in multiprocessors environment
- U shaped tube in Science Lab


### Types Of Deque

**1. Input Restricted Deque**
- Insertion can be done only from rear and deletion of the element can be done from both side(FRONT And REAR)

**2. Output Restricted Deque**
- Deletion from done only from Front End Insertion can be done at both ends.


#### Implementation Of Deque

- Using "collections" built-in Module
- Using List(Basic data structure)

## 1.Using "collections" built-in Module

- Using "collections" built in Module Dequeue Can be implemented

#### Import required following modules
```
from collections import deque
```
#### Initializing  Deque
Syntax:
```
dq=deque(array)
```

Example:
```python
dq=deque([1,2,3,4,5])
```

#### Avialable Option of Deque
```
options=dir(dq)
```

![dequeue](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/dequeue2.png)

#### Primary Operation on Deque
```
1.append
2.appendleft
3.pop
4.popleft
```

### 1.append
insert an element at the right end of the Deque

Syntax:
```
dequeobject.append(element)
```
Example:
```python
#Import deue module from collections
from collections import deque

#Initilizing deque
dq=deque([1,2,3])

#print the deque
print("Normal Deque")
print(dq)


#Append Element at the right end of the deque
#Append 5
dq.append(5)

#print deque after appending 5 element
print("\nDeque After Append 5 at Right Side")
print(dq)
```

Output:
```
Normal Deque
deque([1, 2, 3])

Deque After Append 5 at Right Side
deque([1, 2, 3, 5])
```

### 2.appendleft

insert an element at the left end of the Deque.

Syntax:
```
dequeobject.appendleft(element)
```

Example:
```python
#Import deue module from collections
from collections import deque

#Initilizing deque
dq=deque([1,2,3])

#print the deque
print("Normal Deque")
print(dq)


#Append Element at left end of the deque
#Append 5
dq.appendleft(5)

#print deque after appending 5 element
print("\nDeque After Append 5 at left Side")
print(dq)
```

Output:
```
Normal Deque
deque([1, 2, 3])

Deque After Append 5 at left Side
deque([5, 1, 2, 3])
```

### 3.pop

Delete Element from the right end of the deque.

Syntax:
```
dequeobject.pop()
```

Example:
```python
#Import deue module from collections
from collections import deque

#Initilizing deque
dq=deque([1,2,3])

#print the deque
print("Normal Deque")
print(dq)


#Delete Element from right side
dq.pop()

#print deque after Removing element from right end
print("\nDeque After removing element from right Side")
print(dq)
```

Output:
```
Normal Deque
deque([1, 2, 3])

Deque After removing element from right Side
deque([1, 2])
```


### 4.popleft

Delete Element from left end of the deque
Syntax:
```
dequeobject.popleft()
```

Example:
```python
#Import deue module from collections
from collections import deque

#Initilizing deque
dq=deque([1,2,3])

#print the deque
print("Normal Deque")
print(dq)


#Delete Element from left side
dq.popleft()

#print deque after Removing element from left end
print("\nDeque After removing element from left Side")
print(dq)
```

Output:
```
Normal Deque
deque([1, 2, 3])

Deque After removing element from left Side
deque([2, 3])
```
