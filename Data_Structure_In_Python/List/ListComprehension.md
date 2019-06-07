____________________________

Day 9:Lecture 1
Content: List comprehension
Author:Ravishankar Chavare
Date:07-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*List comprehension*
- Help us to reduce number of line code 
- List comprehension is generally more compact and faster than normal functions and loops for creating list.
- List comprehensions are used for creating new lists from other iterables.
- List comprehension is an elegant way to define and create lists based on existing lists.

Syntax:
Newlist=[expression(item) for item in list]

Example:
Create a list which contains 1 to 10 number 

Using normal for loop
lst=[]
for i in range(1, 11) :
      lst.append(i) 
print(lst) 
#Result:1, 2,3,4,5,6,7,8,9,10

Now using list comprehension

lst=[i for i in range(1,11)]
print(lst) 
#Result:1, 2,3,4,5,6,7,8,9,10


*list comprehension using conditions*

Syntax:
Newlist=[expression(item) for item in list conditions]


Example:
Create a list which contains
2,4,6,8,10

Normal for loop
lst=[]
for i  in range(11) :
    if i%2==0:
        lst.append(i) 
print(lst) 
#Result:2,4,6,8,10

Using List comprehension
lst=[i for i in range(11)  if i%2==0]
print(lst) 
#Result:2,4,6,8,10

You can achieve above sequence using range(2,11,2) also. But we need to understand conditional statement inside list comprehension so we use normal range function. 


*If else in list comprehension.*
Example:
Find out even or odd number from 1 to 10

Using normal for loop
lst=[]
for i in range(1,11):
      if i%2==0:
          lst.append("Even")
       else:
          lst.append("odd") 
print(lst) 
#Result:["odd","Even","odd","Even".....]

Using list comprehension
lst=["Even" if i%2==0 else "odd" for i in range(1,11)]
print(lst) 
#Result:["odd","Even","odd","Even".....]


*Nested Loops in List Comprehension*

Example


Normal for loop
lst=[]
for i in range(5):
      for j in range(i):
          val=[I,j]
          lst.append (val) 
print(lst) 


Hope you enjoying contents😎
[07/06, 10:48 am] ravishankar chavare: ____________________________

Day 9:Lecture 1
Content: List comprehension
Author:Ravishankar Chavare
Date:07-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*List comprehension*
- Help us to reduce number of line code 
- List comprehension is generally more compact and faster than normal functions and loops for creating list.
- List comprehensions are used for creating new lists from other iterables.
- List comprehension is an elegant way to define and create lists based on existing lists.

Syntax:
Newlist=[expression(item) for item in list]

Example:
Create a list which contains 1 to 10 number 

Using normal for loop
lst=[]
for i in range(1, 11) :
      lst.append(i) 
print(lst) 
#Result:1, 2,3,4,5,6,7,8,9,10

Now using list comprehension

lst=[i for i in range(1,11)]
print(lst) 
#Result:1, 2,3,4,5,6,7,8,9,10


*list comprehension using conditions*

Syntax:
Newlist=[expression(item) for item in list conditions]


Example:
Create a list which contains
2,4,6,8,10

Normal for loop
lst=[]
for i  in range(11) :
    if i%2==0:
        lst.append(i) 
print(lst) 
#Result:2,4,6,8,10

Using List comprehension
lst=[i for i in range(11)  if i%2==0]
print(lst) 
#Result:2,4,6,8,10

You can achieve above sequence using range(2,11,2) also. But we need to understand conditional statement inside list comprehension so we use normal range function. 


*If else in list comprehension.*
Example:
Find out even or odd number from 1 to 10

Using normal for loop
lst=[]
for i in range(1,11):
      if i%2==0:
          lst.append("Even")
       else:
          lst.append("odd") 
print(lst) 
#Result:["odd","Even","odd","Even".....]

Using list comprehension
lst=["Even" if i%2==0 else "odd" for i in range(1,11)]
print(lst) 
#Result:["odd","Even","odd","Even".....]


*Nested Loops in List Comprehension*

Example


Normal for loop
lst=[]
for i in range(5):
      for j in range(i):
          val=[I,j]
          lst.append (val) 
print(lst) 


Hope you enjoying contents😎
[07/06, 10:50 am] ravishankar chavare: Two questions for list comprehension:
1.what is the result of *nested loop result given in above tutorial*


2.solve that example using list comprehension..
