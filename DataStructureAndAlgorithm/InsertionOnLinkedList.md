## Node Insertion On Linked List

#### Inserting Element Into Single Linked List
- As compared to array singly list is the best solution to insert a new element at any position such as beginning, end, middle, before and node, after of some node.
- wherein the array if the element at 0 is already present and we insert a new element at 0 positions then the element at 0 indexes is shifted in the right side by one position.
- if there are a small number of elements are present in the list then it is not a problem but consider a huge amount of elements are already present in the list and we are inserting an element at 0 positions then every element is right side shifted by 1.
- But in the linked list when we inserting a new element only one element is shifted to the right side because of these scenario linked list is more powerful than an array.


**There are some different ways to insert an item inside the linked list**

1. Insert node at the Begining
2. Insert node at the end
3. Insert node before another node
4. Insert node after another node
5. Insert node at a specific index
 
## 1.Insert node at the Begining
- Create A method inside SingleLinkedList for insertion of a new node at the beginning
- Now create a Simple node using Node class
```
n_node=Node(data)
```
- Add the link of new Node with start_node data
```
n_node.link=self.start_node
```

- Now Assign self.start_node with the new node
```
self.start_node=n_node
```

![AtBegin](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/insertatbegining.png)

Example:
```python
class Node:
    def init(self,data):
        self.data=data
        self.link=None

#Simple Initialization of Single Linked List
class SingleLinkedList:

    #Constructor of a class contains only one member
    def init(self):
        #Member of the single linked list.
        self.start_node=None #Set to None for Initialization 

    def InsertAtbegin(self,data):
        ''' Used To insert a new Node at the begining of Linked list'''
        n_node=Node(data)
        n_node.link=self.start_node
        self.start_node=n_node

    def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data)
                node=node.link


#Initialize the Object of  SingleLinkedList
s1=SingleLinkedList()

#Check Whether Elements are already present in list or not
s1.TraverseList()
#->

# Add 12 element at the begining of Linked list
s1.InsertAtbegin(12)
#12->

#Add 9 element to the begining of linked list
s1.InsertAtbegin(9)
#9->12

#After adding 12 element to Linked list
s1.TraverseList()

'''
#Result
No Element In List 

9->12->
'''
```


## 2. Insert node at the end
- Now create a Simple node using Node class
```
n_node=Node(data)
```
- To insert an element at the end of the linked list there may be two different situation

**If Linked List is empty**
- if the linked list is empty, all we have to do is set the value of the start_node variable to n_node object
```
if self.start_node is None:
   self.start_node = new_node
   return
```
**If Linked List Already Contains Elements**
- Initialize a variable with start_node
```
nde=self.start_node
```
- iterate through all the nodes in the linked list using a while loop 
```
while nde.link is not None:
	nde=nde.link
```
- Assign last node memory address to already created n_node
```
nde.link=n_node
```
![AtEnd](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/atEnd.png)

Example:
```python
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

    
    def InsertAtEnd(self,data):
        #Create A new Node Using data
        n_node=Node(data)

        #Check If  linked list is empty
        if self.start_node is None:
            #if linked list is empty then assign that new node self.start_node
            self.start_node=n_node
            return

        #If linked list alredy contains elements 
	#The initialize a start variavle using self.start_node
        
	n=self.start_node

        #Iterate till the last Node appears
        while n.link is not None:
            #Assign memory of every next node
            n=n.link
        #if last node is reached then assign
	#that last node memory address to newNode
        n.link=n_node
        
    def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data,end="->")
                node=node.link


#Initialize the Object of  SingleLinkedList
s1=SingleLinkedList()


#Insert Element When Linked list is empty
s1.InsertAtEnd(18)

#After adding 18 element to Linked list at the end
print("\nAdd 18 At the end of the list")
s1.TraverseList()


#Insert Element When Linked list already contains Elements
s1.InsertAtEnd(12)


#After adding 12 element to Linked list at the end
print("\nAdd 12 At the end of the list")
s1.TraverseList()


#Add 9 at the end of the list
s1.InsertAtEnd(9)

#After adding 12 element to Linked list at the end
print("\nAdd 9 At the end of the list")
s1.TraverseList()


'''
#Result
Add 18 At the end of the list
18->
Add 12 At the end of the list
18->12->
Add 9 At the end of the list
18->12->9->

'''
```

## 3.Insert node after another node

- Define a method with 2 parameters with named After_item
```
def After_item(self,data,after):
```

**data**:-new Node which does you want to insert.

**afte**r:-node value to add new node after this "After" node

- initialize the Start of An Object
```
n=self.start_node
```
- Iterate Every Element Until element Found
```
while n is not None:
  #Compare with node data with value
  if n.data==after:
      break
  #Pass the pointer to next Node
  n=n.link
```

- If Element Not Found
 ```
 if n is None:
     print("\nElement not Found:",after) 
  else:
     #Create a New Node
     n_node=Node(data)

     #assign pointer of  new node with the already 
     #available pointer of found node
     
     n_node.link=n.link

     #Now add pointer of aa  founded node with new Node
     n.link=n_node
 ```
![After_item](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/After_Item.png)

Example:
```python
class Node:
    def _init_(self,data):
        self.data=data
        self.link=None

#SimpleInitializationn of Single Linked List
class SingleLinkedList:

    #Constructor of a class contains only one member
    def _init_(self):
        #Member ofthe single linked list.
        self.start_node=None #Set to None for initialization
        
    def InsertAtbegin(self,data):
        ''' Used To insert a new Node at the begining of Linked list'''
        n_node=Node(data)
        n_node.link=self.start_node
        self.start_node=n_node
    
    def After_item(self,data,after):
        #initilize the Start of An Object
        n=self.start_node

        #Iterate Every Element Untill element Found
        while n is not None:
            #Compare with node data with value
            if n.data==after:
                break
            #Pass the pointer to next Node
            n=n.link

        #If Element Not Found
        if n is None:
            print("\nElement not Found:",after)
        else:
            #Create a New Node
            n_node=Node(data)

            #assign pointer of  new node 
	    #with the already available pointer of found node
            n_node.link=n.link

            #Now add pointer of a  founded node with new Node
            n.link=n_node
            
    def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data,end="->")
                node=node.link


#Initialize the Object of  SingleLinkedList
s1=SingleLinkedList()

#Create 4 Elements 18->12->9->7->
s1.InsertAtbegin(7)
s1.InsertAtbegin(9)
s1.InsertAtbegin(12)
s1.InsertAtbegin(18)

#Print Linked List
print("Normal Linked List")
s1.TraverseList()


#Add new Element 5 after 12 element
after=12
s1.After_item(5,after)


#Print Linked List
print("\n\nAfter Adding 5  Element Node after 12 Node")
s1.TraverseList()

'''
#Result
Normal Linked List
18->12->9->7->

After Adding 5  Element Node after 12 Node
18->12->5->9->7-> 
'''
```


### 4.Insert Element Before An Node

- If No element present in linked list return "No Element"
- If only one element present in linked list new node pointer add to that already exists an element
- If Multiple Elements are Present iterate through the loop and if element found to add a reference to that element using the new element


Function Method
```python
def Before_item(self,data,before):
        #If No Element in List
        if self.start_node is None:
            print('No Element')
            return
        
        #If Single Element in List
        if before==self.start_node.data:
            n_node=Node(data)
            n_node.link=self.start_node
            self.start_node=n_node
            return
        
        #initilize the Start of An Object
        n = self.start_node

        #If more than 1 element in linked list
        while n.link is not None:
            #check value with element
            if n.link.data == before:
                break
            n = n.link
        #If item Is not found In List
        if n.link is None:
            print("item not in the list")
        else:
            #Create New Data Node
            n_node = Node(data)
            n_node.link = n.link
            n.link = n_node
```

Example:
```python
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
        
    def InsertAtbegin(self,data):
        ''' Used To insert a new Node at the begining of Linked list'''
        n_node=Node(data)
        n_node.link=self.start_node
        self.start_node=n_node
    def Before_item(self,data,before):
        #If No Element in List
        if self.start_node is None:
            print('No Element')
            return
        
        #If Single Element in List
        if before==self.start_node.data:
            n_node=Node(data)
            n_node.link=self.start_node
            self.start_node=n_node
            return
        
        #initilize the Start of An Object
        n = self.start_node

        #If more than 1 element in linked list
        while n.link is not None:
            #check value with element
            if n.link.data == before:
                break
            n = n.link
        #If item Is not found In List
        if n.link is None:
            print("item not in the list")
        else:
            #Create New Data Node
            n_node = Node(data)
            n_node.link = n.link
            n.link = n_node
            
    def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data,end="->")
                node=node.link


#Initialize the Object of  SingleLinkedList
s1=SingleLinkedList()

#Create 4 Elements 18->12->9->7->
s1.InsertAtbegin(7)
s1.InsertAtbegin(9)
s1.InsertAtbegin(12)
s1.InsertAtbegin(18)

#Print Linked List
print("Normal Linked List")
s1.TraverseList()


#Add new Element 5 before 12 element
before=12
s1.Before_item(5,before)


#Print Linked List
print("\n\nAdding 5  Element Node before 12 Node")
s1.TraverseList()

'''
#Result
Normal Linked List
18->12->9->7->

Adding 5  Element Node before 12 Node
18->5->12->9->7->
'''
```

### 5. Insert at Specific Index
- If index is 1 then directly assign start_node to newly created node
- If not then iterate while loop till index-1 times if node is not none and increment I by one
- if Node is Not None then Assign that new new node value  and change reference with next node
```
n_node=Node(data)
n_node.link=n.link
n.link=n_node
```
Example:

```
class Node:
    def _init_(self,data):
        self.data=data
        self.link=None

#Simple Initialization of Single Linked List
class SingleLinkedList:

    #Constructor of an class
    def _init_(self):
        #Member of single linked list.
        self.start_node=None #Set to None for Initilization
        
    def InsertAtbegin(self,data):
        ''' Used To insert a new Node at the begining of Linked list'''
        n_node=Node(data)
        n_node.link=self.start_node
        self.start_node=n_node
    def Given_index(self,data,index):

        #when index is 1
        if index==1:
            n_node=Node(data)
            n_node.link=self.start_node
            self.start_node=n_node
            return

        #startfrom 1 st node
        i=1
        #initilize start_node
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.link
            i+=1
        if n is None:
            print("out of range index")
        else:
            
            n_node=Node(data)
            n_node.link=n.link
            n.link=n_node
            
    def TraverseList(self):
        if self.start_node is None:
            print("No Element In List ")
            return
        else:            
            node=self.start_node
            while node is not None:
                print(node.data,end="->")
                node=node.link


#Initialize the Object of  SingleLinkedList
s1=SingleLinkedList()

#Create 4 Elements 18->12->9->7->
s1.InsertAtbegin(7)
s1.InsertAtbegin(9)
s1.InsertAtbegin(12)
s1.InsertAtbegin(18)

#Print Linked List
print("Normal Linked List")
s1.TraverseList()


#Addd 5 at 4 index
index=4
s1.Given_index(5,index)


#Print Linked List
print("\n\n5 At 4th index")
s1.TraverseList()

'''
#Result
Normal Linked List
18->12->9->7->

5 At 4th index
18->12->9->5->7->
'''
```
