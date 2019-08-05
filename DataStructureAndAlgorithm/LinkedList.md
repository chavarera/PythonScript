## Linked List

#### Introduction
- Linked list a dynamic data structure used for storing the collection of the data.
- A linked list can store any type of data such as int, float, string, and others.
- A linked list is an ordered collection of values. Linked lists are similar to arrays in the sense that they contain objects in a linear order.
- A linked list is considered a recursive data structure because it has a recursive definition.
- Data in Linked list is not stored in the contiguous memory location. if the contiguous memory location is not available linked list store the data.
- A linked list is linear data structure it contains nodes and each node contains two different parts


![Node](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/sinplenode.png)
#### 1.data :
    Actual Elements are considered as data part.
#### 2.Link :
    It contains the Address of the next node in the linked list.


#### Why use linked lists?
- A linked list saves memory. It only allocates the memory required for values to be stored.
- Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated

#### Disadvantages of Linked List
- When you are looking for value in the linked list, you have to start from the beginning of the chain.
- Random access is not possible because it stores the memory of the next element only.
- Need Some Extra memory to store the memory address of each node in the linked list.

#### Types Of Linked List
1. Single linked list
2. Double linked list
3. Circular linked list
4. Circular Double linked list

### 1. Single linked list
- A single linked list is one in which all nodes are linked together in some linear manner so we can traverse at a time in the same direction only.
- In Single linked list the Last Node contains (None) in Address of the second block.
- In a single linked list, we can traverse in one direction means you can go to the next node with
 node.next you can not traverse in same  for the previous  node for previous you need to start traversing from the beginning of the linked list again
- If link part of the node is None it means there is no next node, mean end of the list

![SingleLinkedList](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/llist.png)

#### How To Create Linked List in Python
Create a Node and assign data and pointer value to each Node

Example:
```python
class Node:
    def _init_(self,val):
        self.val=val
        #Initially Pointer of linked list Points to Nothing
        self.next=None
        
    def Traverse(self,node):
        print('\n\nNode Start Traversing from :{}'.format(node.val))
        while node is not None:
            print(node.val,end="->") # access the node value
            node=node.next          #Move to the next node
            
    def iterate_forward(self):
       print('\n\nNode Start iterating  from :{}'.format(self.val))
       node=self
       while node is not None:
           print(node.val,end="->")
           node=node.next

           
#Initialize the different Nodes
        
n1=Node(12) #Header Node From where linked list started
n2=Node(18)
n3=Node(27)
n4=Node(9)

#Now Add Pointers To every Node in a Linear Way
#12->18
n1.next=n2

#18->27
n2.next=n3

#27->9
n3.next=n4


#Now final Linked list now become like this
#12->18->27->9

#Traverse From Node n1
n1.Traverse(n1)
'''
#Result
Node Start Traversing from :12
12->18->27->9->
'''


#Traverse From node n2
n1.Traverse(n2)
'''
#Result
Node Start Traversing from :18
18->27->9->
'''


#Traverse From node n3
n1.Traverse(n3)
'''
#Result
Node Start Traversing from :27
27->9->
'''


#Get Iterate From Head to Tail Node(Normal Traverse linked list)
n1.iterate_forward()
'''
#Result
Node Start iterating  from :12
12->18->27->9->
'''
```

![LinkedList](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/llis2t.png)
