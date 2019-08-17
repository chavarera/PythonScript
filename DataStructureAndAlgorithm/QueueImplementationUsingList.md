## Queue Implementation using list


### Introduction
- You can Implement Queue Using defualt Data Structure list
- Create A simple Class with any Name
- Initialize Queue in Constructor
```python
def _init_(self):
    self.queue=[]
```
- Append Element At the End of Queue
```python
#Add element at rear part
def Put(self,data):
    self.queue.append(data)
```
- Remove element Which is Inserted First
```python
#Remove Element From Front Part
def Pop(self):
  if self.queue==[]:
      return "Empty Queue"
  else:
      return self.queue.pop(0)
```
- Get Rear Element
```python
#Get Last Element
def GetRear(self):
  if self.queue==[]:
    return "Empty Queue"
  else:
    return self.queue[0]
```

- Get Front Element
```python
#Get First ELment
def GetFront(self):
  if self.queue==[]:
    return "Empty Queue"
  else:
    return self.queue[-1]
```

Example:
```python
#Queue using List
class Queue:
  #Initialize Empty Queue
  def __init__(self):
    self.queue=[]

  #Add element at rear part
  def Put(self,data):
    self.queue.append(data)

  #Remove Element From Front Part
  def Pop(self):
    if self.queue==[]:
        return "Empty Queue"
    else:
        self.queue.pop(0)

  #Get First ELment
  def GetFront(self):
    if self.queue==[]:
        return "Empty Queue"
    else:
        return self.queue[-1]

  #Get Last Element
  def GetRear(self):
    if self.queue==[]:
        return "Empty Queue"
    else:
        return self.queue[0]


#Initilize Queue Object
q=Queue()

#Insert 6 Into Queue
q.Put(6)
print("6 element is Inserted")

#Insert 7
q.Put(7)
print("7 element is Inserted")

#Insert 8
q.Put(8)
print("8 element is Inserted")

#Print Get Front Element
print("Element At Front")
print(q.GetFront())

print("Element At Rear")
#Get Last Element 
print(q.GetRear())

        
#Pop Last Element
q.Pop()

#Now Print Last Element
print("After Popping Rear Element")
print(q.GetRear())
```



output:
```
6 element is Inserted
7 element is Inserted
8 element is Inserted
Element At Front
8
Element At Rear
6
After Popping Rear Element
7
```
