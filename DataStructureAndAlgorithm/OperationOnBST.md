## Operation on Binary Search Tree

### Binary Search Tree Operations

```
1. Insert Element
2. Traverse Tree
    i.Inorder Traversal
    ii.Preorder Traversal
    iii.Postorder Traversal
    
3. Search Element
4. Remove Element
```

### 1. Insert Element
- Use Recursive  pattern to insert new Item  in Binary Search Tree
Follow steps to insert new items in the tree.

- Craete a Normal Node class to creates Nodes for building of Binary search tree
```
class Node:
  def __init__(self,value=None):
    self.value=value
    self.left=None
    self.right=None
    self.count = 1
```

- Create class BST and create Insert and Insert Method Respectively
```
class BST:
    def Insert(self,root,value):
        #create Node using value
        node=Node(value)

        #Perform Insertion Operation here in Recursive manner
        if the root is None Then Return node

        if the root node is not None then perform the following operation
            if root.value==value then just increase counter by 1
            elif value<root.value then assign root.left=self.Insert(root.left,value)
            elif value>root.value then assign root.right=self.Insert(root.right,value)

        #finally return root node
        return root
```
and call above function method from a wraper Method
``` 
 def InsertWrap(self,data):
     root=Node(data[0])
     for value in data[1:]:
        root=self.Insert(root,value)
     #Return the root node
     return node
```
- now create Object of BST
```
t=BST()
data=[9,6,16,18,1,4,7]
t.InsertWrap(data)
```

Full Methods :
```python
#Recusrsive Function to Insert Data into Tree
def Insert(self,root,value):
    node=Node(value)
    if root is None:
      return node
    else:
      if root.value==value:
        root.count+=1
      elif value<root.value:
        root.left=self.Insert(root.left,value)
      elif value>root.value:
        root.right=self.Insert(root.right,value)
    return root

#Wraper Function to Call Insert Method (Call this method first using class object)
def Insertwrap(self,data):
    root=Node(data[0])
    print("Root Node assigned ",data[0])
    for value in data[1:]:
      root=self.Insert(root,value)
      print("Inserted Node",value)
    return root
```


## 2. Traverse Tree

### i.Inorder Traversal

Simple Steps for Inorder Traversal

1. visit the left node if exists
2. print root node Value
3. visit right node if exists
4. go to step 1 if the root node is exists


Example(Recusrsive):
```python
def InOrder(self,root,array):
    if root:
      self.InOrder(root.left,array)
      array.append(root.value)
      self.InOrder(root.right,array)
    return array
```

### ii.Preorder Traversal

Simple Steps for Preorder Traversal

1. print root node Value 
2. visit left node if exists
3. visit right node if exists
4. go to step 1 if the  root node is exists

Example(Recursive):
```python
def PreOrder(self,root,array):
    if root:
      array.append(root.value)
      self.PreOrder(root.left,array)
      self.PreOrder(root.right,array)
    return array  
```

### iii.Postorder Traversal

1. visit the  right node if exists  
2. visit left node if exists
3. print root node Value
4. go to step 1 if the  root node is exists

Example(Recursive):
```python
 def PostOrder(self,root,array):
    if root:
      self.PostOrder(root.left,array)
      self.PostOrder(root.right,array)
      array.append(root.value)
    return array
````


## 3. Search Element

Use the  following steps to search an  element in Binary Search Tree
consider
```
root=Your_binary_search_tree
value=search_element
```

1. if root.value==value then simple return True
2. else compare value with root.value
3. if value<root.value 
    and root.left is present then return Find(root.left,value)
        root.left is not present then return False
4. if value>root.value
    and root.right is present then return Find(root.right,value)
        root.right is not present then return False  

Example:
```python
def Find(self,root,value):
    if root.value==value:
      return True
    else:
      if value<root.value:
        if root.left:
          return self.Find(root.left,value)
        else:
          return False
      else:
        if root.right:
          return self.Find(root.right,value)
        else:
          return False
```

Following Example Contains
```
Insert Element
Inorder Traversal
Preorder Traversal
Postorder Traversal
Search Element
```

Example
```python
class Node:
  def __init__(self,value=None):
    self.value=value
    self.left=None
    self.right=None
    self.count = 1
    
class Tree:
  def __init__(self):
    self.root=None
  
  def Insert(self,root,value):
    node=Node(value)
    if root is None:
      return node
    else:
      if root.value==value:
        root.count+=1
      elif value<root.value:
        root.left=self.Insert(root.left,value)
      elif value>root.value:
        root.right=self.Insert(root.right,value)
    return root
  
  def Insertwrap(self,data):
    root=Node(data[0])
    print("Root Node assigned ",data[0])
    for value in data[1:]:
      root=self.Insert(root,value)
      print("Inserted Node",value)
    return root

  def Find(self,root,value):
    if root.value==value:
      return True
    else:
      if value<root.value:
        if root.left:
          return self.Find(root.left,value)
        else:
          return False
      else:
        if root.right:
          return self.Find(root.right,value)
        else:
          return False
          
  def PreOrder(self,root,array):
    if root:
      array.append(root.value)
      self.PreOrder(root.left,array)
      self.PreOrder(root.right,array)
    return array        
          
  def InOrder(self,root,array):
    if root:
      self.InOrder(root.left,array)
      array.append(root.value)
      self.InOrder(root.right,array)
    return array
    
  def PostOrder(self,root,array):
    if root:
      self.PostOrder(root.left,array)
      self.PostOrder(root.right,array)
      array.append(root.value)
    return array
      

data=[9,6,16,18,1,4,7]
t=Tree()
print("\n_________ Insertion of Node Through List________________")

root=t.Insertwrap(data)
'''
This Binary Search Tree Is Generated Finally

     9
    / \
   6   16
  / \    \
 1   7    18
  \    
   4   

     _9_
    /   \
  _6_    16_
 /   \        \
 1_   7      18
   \    
    4 
       
'''


print("\n___________ Different Tree Traversal_____________________")

print("\nPre Order Traversal")
result=[]
t.PreOrder(root,result)
print(result)

print("\nIn Order Traversal (Sorted)")
result=[]
t.InOrder(root,result)
print(result)

print("\nPost Order Traversal")
result=[]
t.PostOrder(root,result)
print(result)



print("\n___________ Search Element In Tree _____________________")

print("\nIs 4 Present in tree ")
ispresent=t.Find(root,4)
print(ispresent)

print("\nIs 5 Present in tree ")
ispresent=t.Find(root,5)
print(ispresent)
```

Output:
```
_________ Insertion of Node Through List________________

Root Node assigned  9
Inserted Node 6
Inserted Node 16
Inserted Node 18
Inserted Node 1
Inserted Node 4
Inserted Node 7

___________ Different Tree Traversal_____________________

Pre Order Traversal
[9, 6, 1, 4, 7, 16, 18]

In Order Traversal (Sorted)
[1, 4, 6, 7, 9, 16, 18]

Post Order Traversal
[4, 1, 7, 6, 18, 16, 9]

___________ Search Element In Tree _____________________

Is 4 Present in tree 
True

Is 5 Present in tree 
False
```
