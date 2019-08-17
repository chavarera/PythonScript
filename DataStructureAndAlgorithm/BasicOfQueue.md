## Queue

- After Stack, Another fundamental data structure is a queue.
- It's Similar to stack but insertion and deletion of element done according to
"First-In-First-Out" manner.
- In stack Insertion and removal of element done at the one end only, But in **Queue** insertion done at one end and removal of element done at another end so it is first in first out approach.
- The first time added element will be removed First time and second inserted element removed at the second position in this way queue follows a Queue.
- The queue is an Abstract data type in java it is an interface
- Insert Operation done At one point and that one point is called as **Rear**
- Removal Of Element Done at Another End Called as **Front**

![queue](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/queue.png)

### you can Perform the Following Operation on Queue

#### 1. enqueue:
    Adding data element to abstract data types.

#### 2. dequeue:    
    Removing items from the abstract data types

#### 3. peek:
    Peek is used to getting the last item from a queue instead of removing the last element.

### Real-Time  Application of Queue
- Movie Ticket Counter.
- BFS(Breadth-First Search).
- Job Scheduling in Operating System.
- Bank line where people who come first will do his transaction first.
- Keypress sequence in the keyboard.
- The lines or Queue.
- Vehicle waiting to pay toll on the road.


### Implementation

- The queue can be implemented with dynamic arrays as well as a linked list
1. Using **queue** Module
2. Dynamic Array
3. Linked List


### Perform Operation on the queue using the queue python module

#### 1.Initialize the queue
- for initializing the queue data structure using *queue* Module  first import *queue* model in script
```
import queue
```
- After the import of the queue module now initialize the queue object.
```
que=queue.Queue(maxszie=<Size_of_queue>)
```
Following are the two common terms used in queue
**1. queue Overflow**
    - when we try to insert data element into a Queue above is max size, it is called queue *OverFlow.*
**2. queue Underflow**
    - when we try to remove an element from an empty queue then its called as *Underflow.*

Example:
```python
import queue

#Initilize the queue by using maxsize
que=queue.Queue(maxsize=5)
print(que)
```

Output:
```
#Result:
<queue.Queue object at 0x00000255E2267240>
```


### 2.Insertion and removal item from queue
- Inserting element at end of queue
Syntax:
```
Queue.put(data_Element)
```
Example:
```
#import required module
import queue

#Initilize the queue by using maxsize
que=queue.Queue(maxsize=5)
print(que)


#Insert 6 into queue
que.put(6)
print("6 Inserted")

#insert 7
que.put(7)
print("7 inserted")

#Get Element From Queue
print(que.get())
print("6 is Removed")

#Get Next Element From Queue
print(que.get())
print("7 is Removed")
```

Output:
```
<queue.Queue object at 0x000001F8B9BF3860>
6 Inserted
7 inserted
6
6 is Removed
7
7 is Removed
```
