## Updating The Node Value

- Return **"No Element"** if linked list is Empty
```
if n is None:
   print("\n No Element in List")
   return
```
- If linked list contains element iterate linked list using while loop
```
while n is not None:
    n=n.link
```    
- and at every loop compare node data value with required node (For Deletion)
```
n.data==data
```
- If Node Found break the loop
```
if n.data==data:
   break
```
- And Assign Data of that node of next node data and link of that node to be next of next node
```
n.data=Replace_Value
```
Function:
```python
def UpdateNode(self,data,replace):
  #initialize the Head Node (start_node)
  n=self.start_node
  if n is None:
    print("\n No Element in List")
    return
  #Iterate through Whole List
  while n is not None:
    # if Node data found break the loop
    if n.data==data:
      break
    n=n.link

  #If Element is not found in the list
  if n is None:
    print("Element Node Not Found in Linked List")
  else:
    #if node found assign value to that node
    n.data=replace
```

Full Example:
```python
class Node:
  def __init__(self,data):
    self.data=data
    self.link=None

class SingleList:
  def __init__(self):
    self.start_node=None
  def Push(self,data):
    n_node=Node(data)
    n_node.link=self.start_node
    self.start_node=n_node
    return
  def Traverse(self):
    n=self.start_node
    while n is not None:
      print(n.data,end="->")
      n=n.link

  def UpdateNode(self,data,replace):
    #initialize the Head Node (start_node)
    n=self.start_node
    if n is None:
      print("\n No Element in List")
      return
    #Iterate through Whole List
    while n is not None:
      # if Node data found break the loop
      if n.data==data:
        break
      n=n.link

    #If Element is not found in the list
    if n is None:
      print("Element Node Not Found in Linked List")
    else:
      #if node found assign value to that node
      n.data=replace


#Simple Initialize the single linked list
s1=SingleList()

#Add Node 5,12,18
s1.Push(5)
s1.Push(12)
s1.Push(18)

#Print Normal Linked List
print("\nNormal Linked List")
s1.Traverse()

#Replace 12 Node with 7
replace=7
s1.UpdateNode(12,replace)

#Print Normal Linked List
print("\n\nLinked List After Replace 12 Node With 7")
s1.Traverse()

```

Output:
```
Normal Linked List
18->12->5->

Linked List After Replace 12 Node With 7
18->7->5->
```
