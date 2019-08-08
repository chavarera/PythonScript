## Stack

### Basic of Stacks
- Simple Stack meaning arranging object on over another.
- Stack plays a very vital role in data structure and in the algorithm in any programming language.
- A Stack is a Container of objects that are inserted and removed according to Last-In-First-Out (LIFO) Principal.
- The stack data structure allows operation at only one end that end is called top.
- The stack is a Recursive  data structure according to the structural definition of the stack

1. A stack is either empty
or
2. It consists of one top and rest of element stacked together

![Stack](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/stack.png)
### Stack support two different operations
### 1. Push(Insert ELement)
	which adds an element to the collection. 
### 2. Pop(Remove Element)
	removes the most recently added element that was not yet removed.

- We can add an element or remove element only from the end of the stack called top of the stack.

### Some Real-Time Example Application of Stacks
- Stack of dinner plates.
- Stack of Moulded chairs.
- Web browser back button(History is Saved in stack LIFO manner)
last visited page saved in top of the stack and when we press back button top of the URL stack is opened in a web browser.
- undo and redo operation in text Editors.
- Bangle set - One has to remove the last inserted bangle to insert a new bangle in the set.
- A set of books - You can only remove the last inserted book to insert a new book in the stack.
 

### Implementation
- The stack is an Adapter class means that stack is built on top of other data structure.

The stack can be implemented using 
1. List
2. Array List
3. Linked list
4. Vector


#### Implementation Of Stack Using List
create empty stack using list
```
self.stack=[]
```

Function:
```python
def __init__(self):
        self.stack=[]
```

Full Example:
```python
#Create A Stack Class
class STACKS:
    def __init__(self):
        self.stack=[]

#Initilize Stacks Objects
s1=STACKS()
```
