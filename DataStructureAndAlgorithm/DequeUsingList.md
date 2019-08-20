## Implementation of Deque Using List


#### Initialize blank Deque Using List
```
def __init__(self):
    print("Initialize blank Deque Using List")
    self.dq=[]
```

#### Add Element at Left End Of Deque
```
def AddLeft(self,data):
    '''Add Element at Left End Of Deque'''
    self.dq.insert(0,data)
```

#### Add Element at Right End Of Deque
```
def AddRight(self,data):
    '''Add Element at Right End Of Deque'''
    self.dq.append(data)
```
#### Remove Element From  Left End Of Deque
```
def PopLeft(self):
    '''Remove Element From  Left End Of Deque'''
    self.dq.pop(0)
```

#### Remove Element From  Right End Of Deque
```
def PopRight(self):
    '''Remove Element From  Right End Of Deque'''
    self.dq.pop()
```
  

Full Example
```python
class Deque:
  def __init__(self):
    print("Initialize blank Deque Using List")
    self.dq=[]
    
  def AddLeft(self,data):
    '''Add Element at Left End Of Deque'''
    self.dq.insert(0,data)
    
  def AddRight(self,data):
    '''Add Element at Right End Of Deque'''
    self.dq.append(data)
    
  def PopLeft(self):
    '''Remove Element From  Left End Of Deque'''
    self.dq.pop(0)
    
  def PopRight(self):
    '''Remove Element From  Right End Of Deque'''
    self.dq.pop()
    
  def TopLeft(self):
    '''Top Left Element'''
    return self.dq[0]
    
  def TopRight(self):
    '''Top Right Element'''
    return self.dq[-1]
    
  def Show(self):
    return self.dq
d=Deque()
print("\nBlank Deque")
print(d.Show())

#Add Element 5
d.AddRight(5)

#print deque
data=d.Show() 

print("\nDeque After Adding 5")
print(data)


#Add Element At the Right End
#Add 7
d.AddRight(7)

#Add 9
d.AddRight(9)

print("\nDeque After Adding 7 and 9 at Right end")
print(data)


#Add 6 element at Left Side End
d.AddLeft(6)

print("\nDeque After Adding 6 at Left End")
print(data)
#----------------------------TOP ELEMENT------------------------------
print("\nTop Element At Right End")
right=d.TopRight()
print(right)


print("\nTop Element At Left End")
left=d.TopLeft()
print(left)
#----------------------------Remove Element---------------------------

#Remove 6 From Right End
d.PopRight()

print("\nDeque After Remoing Element from Right End")
print(data)

#Remove 6 From Left End
d.PopLeft()

print("\nDeque After Remoing Element from Left End")
print(data)
```

Output
```
Initialize blank Deque Using List

Blank Deque
[]

Deque After Adding 5
[5]

Deque After Adding 7 and 9 at Right end
[5, 7, 9]

Deque After Adding 6 at Left End
[6, 5, 7, 9]

Top Element At Right End
9

Top Element At Left End
6

Deque After Remoing Element from Right End
[6, 5, 7]

Deque After Remoing Element from Left End
[5, 7]
```
