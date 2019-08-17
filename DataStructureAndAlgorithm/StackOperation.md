## Stack Operation

In Following Example We are Implementing stack with the list data structure 
```
1. Push
2. Pop
```

### 1.Push()

- Pushing element at the top of the stack and move cursor of top to next Inserted Element.
- We can implement it with the help of *List* Data structure Because the stack is built on top of the basic data structure.
- Add an element to top of the stack.

Function:
```python
def Push(self,data):
  '''This Will accept Element And Append to existing stack'''
  self.stack.append(data)
```

Example:
```python
class STACKS:
  
  def __init__(self):
    self.stack=[]
      
  def Push(self,data):
    '''This Will accept Element And Append to existing stack'''
    self.stack.append(data)
      
  def Show(self):
    return self.stack
    
s1=STACKS()

#Empty Stack
print("Empty Stack")
print(s1.Show())

#Push 5 Element
s1.Push(5)

#Add 8 Element to Stack
s1.Push(8)

#Stack With ELement
print("\nStack With ELement")
print(s1.Show())
```

Output:
```python
Empty Stack
[]

Stack With ELement
[5, 8]
```


### 2.Pop
- Poping the element means Removing the top element from the stack and move down cursor to next element. 
- Remove element from the top of the stack


Function:
```python
def Pop(self):
  '''This will Remove the element from top of the stack'''
  self.stack.pop()
```
Example:
```python
class STACKS:
  def __init__(self):
    #Initialize Empty Stack
    self.stack=[]
      
  def Push(self,data):
    '''This Will accept Element And Append to existing stack'''
    self.stack.append(data)

  def Pop(self):
    '''This will Remove the element from top of the stack'''
    self.stack.pop()
      
  def Show(self):
    return self.stack
    
s1=STACKS()

#Empty Stack
print("Empty Stack")
print(s1.Show())

#5,8,18,21
s1.Push(5)
s1.Push(8)
s1.Push(18)
s1.Push(21)
s1.Push(12)


#Stack With ELement
print("\nStack With ELement")
print(s1.Show())


#pop Last element From Stack
s1.Pop()


print("\nStack Element After Poping last Element")
print(s1.Show())
```

Output:
```
Empty Stack
[]

Stack With ELement
[5, 8, 18, 21, 12]

Stack Element After Poping last Element
[5, 8, 18, 21]
```


### We Can Create Some Custom Options For Stack

1. Check Top Element
2. Check Empty Stack

#### 1.Check length of stack

Function:
```python
def Top(self):
  ''' This Will Return The Top Of the Stack if Empty Then It will Return -1'''
  if self.stack==[]:
      return "Stack is Empty"
  else:
      return self.stack[-1]
```

### 2. Check Stack is Empty Or Not:

Function:
```python
def IsEmpty(self):
  '''Return True If stack is empty else Return False'''
  if self.stack==[]:
      return True
  else:
      return False
```

![StackOperation](https://github.com/chavarera/PythonScript/blob/master/DataStructureAndAlgorithm/stackOperation.png)

Full ALL Example:
```python
class STACKS:
  def __init__(self):
    #Initialize Empty Stack
    self.stack=[]
      
  def Push(self,data):
    '''This Will accept Element And Append to existing stack'''
    self.stack.append(data)

  def Pop(self):
    '''This will Remove the element from top of the stack'''
    self.stack.pop()

  def Top(self):
    ''' This Will Return The Top Of the Stack if Empty Then It will Return -1'''
    if self.stack==[]:
        return "Stack is Empty"
    else:
        return self.stack[-1]
      
  def IsEmpty(self):
    '''Return True If stack is empty else Return False'''
    if self.stack==[]:
        return True
    else:
        return False
      
  def Show(self):
    '''Retrun Stack All Element'''
    return self.stack

#Initialize The Stack Object    
s1=STACKS()


#Empty Stack
print("Empty Stack")
print(s1.Show())

#Check Is Stack is Empty OR Not
print("\nIs Stack Is Empty")
print(s1.IsEmpty())

#5,8,18,21
s1.Push(5)
s1.Push(8)
s1.Push(18)
s1.Push(21)
s1.Push(12)


#Stack With ELement
print("\nStack With ELement")
print(s1.Show())



#pop Last element From Stack
s1.Pop()


print("\nStack Element After Poping last Element")
print(s1.Show())


#Get Current Top Element
print("\nTop Of The Stack")
print(s1.Top())


#Check Is Stack is Empty OR Not
print("\nIs Stack Is Empty")
print(s1.IsEmpty())
```

Output:
```
Empty Stack
[]

Is Stack Is Empty
True

Stack With ELement
[5, 8, 18, 21, 12]

Stack Element After Poping last Element
[5, 8, 18, 21]

Top Of The Stack
21

Is Stack Is Empty
False
```
