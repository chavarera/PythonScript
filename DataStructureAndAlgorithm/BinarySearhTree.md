## Binary Search Tree

### Binary Search Tree
- As we already Know A binary tree is a tree whose children are never more than two same features are in a binary search tree along with some criteria to build it.
- Binary Search Tree is one type of implementations specially designed especially for Searching.
- In a Binary search tree, all the nodes are arranged in a specific order
- A tree can be called as a binary search tree if and only if the maximum number of children of any of the nodes is two 
and the left child is always smaller than the right child
- A Binary Search Tree or Ordered Binary Tree is one type of binary tree where the nodes are arranged in order

- If you perform Inorder Traversal on Binary search tree you will get sorted values of inserted items


Binary Search Tree (BST) is a special type of Binary Tree that follows the following condition:
```
- All the left nodes(left Subtree recursively) have a smaller value than the value of the parent node.
- All the right nodes((right Subtree recursively)) have values greater than or equal to the parent node.
```

Example 1
```
    5
   / \    
  3   9
```

Example 2
```
        50
     /     \
    25      75
   /  \    /  \
 20   30  70  80
```

Example 3
```
        8
       / \
      7   12
     /   /  \
    4   11   28
   / \        
  2   5        
```

Binary Search Tree (BST) is a special form of Binary Tree data structure where each node has a comparable value, 
and smaller valued children attached to the left and larger valued children attached to the right.

Following Example Is not Binary Search Tree
```
        7
       /  \
      9    12
```
Because here 9 is placed at the left side of 7 which is wrong because the only small element can be placed at the left side tree of the root node.


Simple Example To Create A Binary Tree
```python
class Node:
  def __init__(self):
    self.value=value
    self.left=None
    self.right=None

root=Node(5)
root.left=Node(3)
root.right=Node(9)

'''
Above Example Create A Simple Binary Search Tree
    5
   / \
  3   9
'''
```

In Next Lessons, We Are going to create some concrete example of Binary Search Tree
```
- Insert element
- Search element
- Delete element
- Traverse elements
- Sort element
```
