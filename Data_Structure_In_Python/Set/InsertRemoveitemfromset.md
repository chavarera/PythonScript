____________________________

Day 12:Lecture 1
Content: Insert, Remove Items 
Author:Ravishankar Chavare
Date:09-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*Add and Remove Element in Set*

*1.Add Items to Set*
- To add element inside set there are two built in function
1. add()
2. update()

*1.add()*
- To add one item to a set use the *add()* method.
- The set add() method adds a given element to a set if the element is not present in the set
Syntax:
setname.add(element)

Example:
color={"red","green","blue"}
#add new element "black" to set
color.add("black")
print(color)
#result:{"red","green","black","blue"}

-If the element is alredy present in the set then it will not added again to set ,
because set do not contain any duplicate value.

Example:
color={"red","green","blue"}
#add new element "blue" to set
color.add("blue")
print(color)
#Result:{"red","green","blue"}


*2.update()*:
- Add multiple items to a set, using the *update()* method
Syntax:
setname.update(iterable object)

Example:
color={"red","green","blue"}
#Add "black" and "orange" to set
color.update(["black","orange"])
print(color)

#Result:{'orange', 'red', 'green', 'blue', 'black'}
________________________________________

*2.Remove Items from list*
- use the *remove()*, or the *discard()* method.

*1.remove()*
- remove() method  removes the element from the set only if the element is present in the set.
- If the element is not present in the set, then an error or exception is raised.

Example:
color={"red","green","blue"}
#remove "red"
color.remove("red")
print(color)
#Result:{"green","blue"}

Example:
color={"red","green","blue"}
#remove "black"
color.remove("black")
#Result:KeyError: 'black'

*2.discard()*
- *discard()* method removes the element from set only if the element is present in the set.
-  If the element is not present in the set, then no error or exception is raised.

Syntax:
setname.discard(element)

Example:
color={"red","green","blue"}
#remove "black"
color.remove("black")
#Result:KeyError:{"red","green","blue"}

______________________________________

*3.Change Items in set*
- Once a set is created, you cannot change its items.
