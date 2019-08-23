## Tree Data Structure
![tree](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/tree.png)

### Introduction
- Tree is a hierarchical data structure which stores the information naturally in the form of hierarchy style.
- Tree is a data structure that is similar to our trees in nature which is most powerful and advanced datastructure.
- Trees are well known as a non-linear Data Structure. It doesn’t store data in a linear way. 
- It organizes data in a hierarchical way.
- Tree is a collection of entities called node connected by edges.
- Unlike trees in nature, the tree data structure is upside down: the root of the tree is on top.
- A tree consists of nodes and its connections are called edges. The bottom nodes are also named leaf nodes.
- Python doesn't have any built in way to create tree data structture but we can implement using list and other data structure.


### Real Time Application OF Trees
- Database Application.
- File System in Unix or Linux.
- Imagine a family tree with all generation relationship: grandparents, parents, children, siblings, etc. 
We commonly organize it in a hierarchical way.

- A tree is an abstract data type that stores elements hierarchically. With the exception of the top element, 
each element in a tree has a parent element and zero ormore children elements

### Advantages of Tree
- Tree reflects structural relationships in the data.
- Tree 
It provides an efficient insertion and searching operations.
Trees are flexible. It allows to move subtrees around with minimum effort.

### Some Important Terminology in Tree Data Structure

- Node
- Edge
- Root Node
- Leaf Node
- Parent Node
- Child Node
- Siblings
- Degree
- Height
- Depth
- Level

#### Node
- Where Node have Zero or more children.
- Each Node contains value and some Links to its child.
- The Connection between two node is called as *edge*.
![node](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/node.png)

#### Edge
- In any Given tree the the connection between two node is called as *edge*.
- If  "N" no of Nodes present in the tree the the count of edges should be "N-1" times.
![edge](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/edge.png)

#### Root node
- Root node is the very first or parent node in tree.
- Normally a tree start with root and then goes up to its crown so root node is the first node of the given tree
![root](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/root.png)

#### Leaf Node
- A Node without any children is called leaf node or terminal nod.
- In hierarchy Leaf node Placed at the End of the tree where tree nodes do not have any child
![leaf](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/leaf.png)

#### Parent Node
- A Node Which hase a branch from it to any other node such node is called as parent node.
- Predecessor of any node is called parent node.
- A Normal Node which has a child Node is called as parent node.
![parent](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/parent.png)

#### Child Node
- A Node which has a link from its parent node is called as child Node
- descendant of any node is called as Child Node
- Any Successor of node is called as Child node.
![child](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/child.png)


#### Siblings
- The Node which has same parent is called as siblings.
- In simple word Nodes with the same parent are sibling nodes.
![siblings](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/siblings.png)

#### Degree
Degree Of Node:
	total number of direct children of that node is called degree of that node.

Degree Of Tree
	The degree of the tree is the total number of it's children. 
![degree](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/degree.png)

#### Internal Node
- Every node who has at least one child is called as internal node
- all Non-Leaf Nodes are called as Internal Node.
- We can also call Non-Terminal Node to Internal node.
![internalcode](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/internalcode.png)

#### Level
- The Each Step From Top(Root Node) to Bottom is called as level of the tree
- level of treee count started from 0.
- Root Node is placed at 0th level.
![level](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/level.png)

#### Depth
- Total no of edges from root node to specific given node is called the Depth of the node.
- Depth of Root Node is Zero(0)
- Depth of a tree is the total number of edges from root node to a leaf node in the longest path.
![depth](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/depth.png)

#### Height
- Total number of edges that lies on the longest path from any leaf node to a particular node is called as height of that node.
- Height of leaf node is always 0.
![height](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/tree/height.png)
