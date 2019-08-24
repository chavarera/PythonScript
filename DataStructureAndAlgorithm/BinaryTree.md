## Binary Tree
- A Binary Tree is simply a data structure with a 'key' element, and two children, say 'left' and 'right'.
- A tree whose element has at most 2 children is called Binary Tree.
- In Binary tree, every element has at most 2 children only we typically name them the left and right child.
- A common kind of tree is a binary tree, in which each node contains a reference to two other nodes (possibly None)
![BinaryTree](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/binarytree.png)
### Binary Tree Parts
```
- value
- pointer to the left child
- pointer to the right child
```

### Building Binary Tree
Create a Node to represent a binary tree
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
```

When creating any node in tree initially left and the right pointer can be should be None.
```python
#Create Root Node 1
n1=Node(1)

#Create Node 2
n2=Node(2)

#Create Node 3
n3=Node(3)

#Add 2 node to the left side of root node
n1.left=n2

#add 3 node to the right side of root node 1
n1.right=n3
```

Full Example:
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value

#Create Root Node 1
n1=Node(1)

#Create Node 2
n2=Node(2)

#Create Node 3
n3=Node(3)


#Add 2 node to the left side of root node
n1.left=n2

#add 3 node to the right side of root node 1
n1.right=n3
```


### Tree Traversal
There are three ways of traversing a binary tree 
```
- pre-order, 
- in-order,
- post-order.
```

### Pre-Order Traversal
- First Visit Root node and print It.
- Traverse left subtree
- Traverse Right subtree

![preorder](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/preorder.png)

```python
def Preorder(self,root):
    if  root:
      print(root.value)
      self.Preorder(root.left)
      self.Preorder(root.right)
```

### In-Order Traversal

- Traverse left subtree
- Visit the Root node and print It.
- Traverse Right subtree

![inorder](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/inorder.png)

```python
def Inorder(self,root):
    if  root:
      self.Inorder(root.left)
      print(root.value)
      self.Inorder(root.right)
```

### Post-Order Traversal

- Traverse left subtree
- Traverse Right subtree
- Visit the Root node and print It.

![postorder](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/postorder.png)

```python
def Postorder(self,root):
    if  root:
      self.Postorder(root.left)
      self.Postorder(root.right)
      print(root.value)
```

Full Example:
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
class Tree:
  def __init__(self):
    self.root=None
    
  def Preorder(self,root):
    if  root:
      print(root.value)
      self.Preorder(root.left)
      self.Preorder(root.right)
      
  def Inorder(self,root):
    if  root:
      self.Inorder(root.left)
      print(root.value)
      self.Inorder(root.right)
        
    
  def Postorder(self,root):
    if  root:
      self.Postorder(root.left)
      self.Postorder(root.right)
      print(root.value)

#Create Root Node    
root = Node(1) 
root.left= Node(2) 
root.right= Node(3) 
root.left.left= Node(4) 

#Create Object of Simple Tree
t1=Tree()

#preorder Traversal
print("Preorder")
t1.Preorder(root)

#Inorder Traversal
print("Inorder")
t1.Inorder(root)

#Postorder Traversal
print("Postorder")
t1.Postorder(root)
```

Output:
```
Preorder
1
2
4
3
Inorder
4
2
1
3
Postorder
4
2
3
1
```
