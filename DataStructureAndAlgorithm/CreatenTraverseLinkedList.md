## Create and traverse linked list

Basic Operation
1. Create Node
2. Create a Linked List
3. Traverse Linked list

### 1. Create A Node

- create a normal class and initialize two parameters
- We already know that in single linked list node contains two block
```
1. data block.
2. memory address of the next Node.
```
![Simple Node](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/sinplenode.png)
- At the time of node initialization, the memory address of the current node is set to be None
- Our node class will contain two member variables data and link. 
- The value of the data will be set by the value passed through the constructor.
- The link value  will be initially set to None

Example:
```python
class Node:
    def _init_(self,data):
        self.data=data
        self.link=None
```

### 2. Create Single Linked list Class

- Create a Class for a single linked list and write down different methods for insert item, remove the item and traverse a linked list.
- Initially, Singly linked list pointing to the starting or the first node of the linked list.
- The Single linked list contains the only member that is start_node which is initially Set to None Because the linked list will be empty
at the time of the creation of the linked list.
![singleNone](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/singlelinkedlist.png)

Example
```python
#Create Node
class Node:
    def _init_(self,data):
        self.data=data
        self.link=None


#Simple Initialization of Single Linked List
class SingleLinkedList:
    #Constructor of a class contains only one member
    def _init_(self):
        #Member of the single linked list.
        self.start_node=None #Set to None for Initialization 
```

### 3.Traversing a linked list
- **self.start_node** is the current node and if it is **None** then the Linked list is empty.
```python
if self.start_node is None:
    print("No Element In List ")
    return
```
- if **self.start_node** is not **None** then print the node with **node.data**.
- And Assign Node to next link node 
```python
node=node.link
```
![Traverse](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/traverselinkedkist.png)

Example:
```python
def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data)
                node=node.link    
```
**self.start_node** is the start node of the single linked list so it assigned to a node if it is  **None** as start node and traverse One By one
