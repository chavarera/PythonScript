____________________________

Day 12:Lecture 2
Content: mathematical operation on set
Author:Ravishankar Chavare
Date:10-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*Set Operation*

Sets can be used to carry out mathematical set operations following different operation on set can be performed 

1. Union (|)
2. Intersection (&)
3. difference (-)
4. symmetric difference (^)


*1.union()*
- Two sets can be "added" together.
- Union is performed using *|* operator same can be achived using built in function *union()*.

Syntax:
setA=set()
SetB=set()
result=SetA | SetB 

OR

result=SetA.union(SetB)

Example:
A={1,5,2}
B={6,7,8,9}
#using built in method .union()
result=A.union(B)
print(result)
#Result:{1, 2, 5, 6, 7, 8, 9}

#Using | operator
result1=A | B
print(result1)
#Result:{1, 2, 5, 6, 7, 8, 9}

_____________________________________

*2.Intersection*
- A new set can also be constructed by determining which members two sets have "in common"
- Intersection is performed using *&* operator same can be achived using built in function *intersection()*.

Syntax:
setA=set()
SetB=set()
result=SetA & SetB 

OR

result=SetA.intersection(SetB)

Example:
A={1,5,2}
B={3,2,1,6,8,7}

#using built in method .intersection()
result=A.intersection(B)
print(result)
#Result:{1, 2}

#Using & operator
result1=A & B
print(result1)
#Result:{1, 2}
______________________________________

*3. Difference*:
- Two sets can also be "subtracted".
- difference can be performed using *-* operator or same thing can be achieved using *difference()*.
- here A - B Result is Different result than B - A.

A-B:The elements included in A, but not included in B.
B-A:The elements included in B, but not included in A.

Syntax:
setA=set()
SetB=set()
result=SetA - SetB 

OR

result=SetA.difference(SetB)


Example:
A={1,2,3,5,4}
B={2,4,8,6,9}
#using built in method .difference()
result=A.difference(B)
print(result)
#Result:{1, 3, 5}

#Using - operator
result1=A - B
print(result1)
#Result:{1, 3, 5}
______________________________________

*4. symmetric Difference*:
- The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
- symmetric Difference can be performed using *^* operator or same thing can be achieved using *symmetric_difference()*.

Syntax:
setA=set()
SetB=set()
result=SetA ^ SetB 

OR

result=SetA.symmetric_difference(SetB)

Example:
Example:
A={1,2,3,5,4}
B={2,1,8,6,9}
#using built in method .symmetric_difference()
result=A.symmetric_difference(B)
print(result)
#Result:{3, 4, 5, 6, 8, 9}

#Using ^ operator
result1=A ^ B
print(result1)
#Result:{3, 4, 5, 6, 8, 9}
