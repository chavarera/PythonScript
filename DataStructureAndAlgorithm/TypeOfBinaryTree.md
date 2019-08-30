## Types of Binary Tree

### Types Of Binary Tree
```
1. Full Binary Tree
2. Complete Binary Tree
3. Perfect Binary Tree
4. Balanced Binary Tree
5. Degenerate tree
```

## 1.Full Binary Tree
- Every Node has either 0 or 2 Childern
- In full binary tree every Internal node have 2 Child while every terminal have 0 Child.
- there is no node in a full binary tree, which has one child node.

#### Algorithm To check Full Binary Tree or Not
1. If Node is NUll Then it is a Full binary tree
2. IF Node has empty left and right subtree then it is a full binary tree.
3. If binary tree has left and right subtree In this case recursively check if the left and right sub-trees are also full binary trees themselves.

Example Of Full Binary Tree
```
     1
   /   \
  2     3 
 / \
4   6
```

Example:
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
class Tree:
  def __init__(self):
    self.root=None
    
  def ChekFullBinary(self,root):
    # If Root is Empty Then Full Binary Tree
    if root is None:
      return True
    #If Left And Right Subtree is None Then Full Binary Tree
    if root.left is None and root.right is None:
      return True
    
    #If Left and Right binary tree present then check recursively
    if root.left is not None and root.right is not None:
      return self.ChekFullBinary(root.left) and self.ChekFullBinary(root.right)
      
    #If Above All conditions Fails Then it is not a Fulll Bnary Tree
    return False
#Create Root Node    
root = Node(1) 
root.left= Node(2) 
root.right= Node(3) 
root.left.left= Node(4) 
root.left.right= Node(6) 

#Create Object of Simple Tree
t1=Tree()
"""
Example Of Full Binary Tree
     1
   /   \
  2     3 
 / \
4   6


This is Not Full Binary Tree
     1
   /   \
  2     3 
 / 
4 
"""
print("Is This Full Binary Tree")
print(t1.ChekFullBinary(root))
```

Output:
```
Is This Full Binary Tree
True
```

## 2. Complete Binary Tree

- A complete binary tree is a binary tree in which every level, except possibly the last, 
is completely filled, and all nodes are as far left as possible. 

To Satisfy Complete Binary Tree We Ensure following Conditions Should be True
- All Levele are completely filled except the possibly last level)
- Node in the Last Level are Filled from left to right

Example OF Complete Binary Task
```
     1
   /   \
  2     3 
 / \    / \	
4   5  6   7
```

Second Example
```
     1
   /   \
  2     3 
 / \    / 	
4   5  6  
```
Following is not Complete Binary tree beacause 7 node is placed at the right side of 3 where leftside of 3 is blank
```
     1
   /   \
  2     3 
 / \     \	
4   5     7
```

## 3.Perfect Binary Tree

A Tree s called perfect binary tree if it satisfy forllowing two condtions

1. All Internal node must have 2 children
2. All Leaf Node at the same level

**Note**: A Perfect Binary Tree is Always a Complete and Full Binary Tree

Example oF complete binary task
```
     1
   /   \
  2     3 
```
Example 2:
```
     1
   /   \
  2     3 
 / \    / \	
4   5  6   7
```


## 4.Balanced Binary Tree

- A tree is called balanced binary tree if it follows following constraints.
- For Every Node 
height_of_left_subtree-heigt_of_right_subtree<=1


Example:
```
     1
   /   \
  2     3
 /     
4     

4 Balance :0
2 Balance :1
1 Balance :1
3 Balance :0
```

Example 2:
```
       1
     /   \
    2     3
   /     
  4 
 /
5

Balance of 2:2-0 =2
which is greator than 1 so This is not balanced Binary Tree
```

Example To Check Balanced Tree:
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
class Tree:
  def __init__(self):
    self.root=None
  
  def GetHeight(self,root): 
    if root is None: 
        return 0
    return max(self.GetHeight(root.left), self.GetHeight(root.right)) + 1
    
  def IsBalanced(self,root): 
    #If Root is None Then return True
    if root is None: 
        return True
    #Get Height of Left Balance
    lftheight = self.GetHeight(root.left) 
    
    #Get Height Of  Right Balance
    rgtheight = self.GetHeight(root.right) 
    
    if (abs(lftheight - rgtheight) <= 1) and self.IsBalanced(root.left) is True 
    and self.IsBalanced(root.right) is True: 
        return True
    return False
          
#Create Root Node    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 


#Create Object of Simple Tree
t1=Tree()
"""
    1
   /   \
  2     3
 /     
4 

"""

print("Is IsBalanced Tree")
print(t1.IsBalanced(root))
```

Output:
```
Is IsBalanced Tree
True
```
   

## 5. Degenerate tree

A tree is called Degenerate tree if it satisfy following Conditions

1. Every Internal Node has only one child

- As Performance wise degenerate tree is Same as linked list

Example 1:
```
       1
     /   
    2    
   /     
  4 
 /
5
```

Example 2:
```
1
 \
  2
   \
    3
```
Example:3
```
    1
   /
  2
   \
    3
    /
   4
```	

Example to check IsDegenerateTree
```python
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
class Tree:
  def __init__(self):
    self.root=None
    
  def IsDTree(self,root):
    if root is None:
      return True
    if root.left is not None:
      if root.right is not None:
        return False
      else:
        return self.IsDTree(root.left)
    if root.right is not None:
      if root.left is not None:
        return False
      else:
        return self.IsDTree(root.right)
    return True
   
   
#Create Root Node    
root = Node(1) 
root.left= Node(2) 
root.left.right=Node(3)
root.left.right.left=Node(4)
#Create Object of Simple Tree
t1=Tree()
"""
    1
   /
  2
   \
    3
    /
   4
"""

print("Is Degenerate Tree")
print(t1.IsDTree(root))
```

Output:
```
Is Degenerate Tree
True
```
