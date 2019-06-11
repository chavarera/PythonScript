____________________________

Day 11:Lecture 2
Content: Basic of set
Author:Ravishankar Chavare
Date:09-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*Set*

*What is a set in Python?*
- A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
- Every element is unique and must be immutable (which cannot be changed). but set itself mutable objects
- Sets are unordered, so the items will appear in a random order.
*How to create a set?*
- you can create a set using curly braces or using built in function set()

Synatx:
setname={element}
setname1=set(elements)

Example:
You can not create a blank set like this
blankset={}
print(type(blankset)) 

#Result:this will create object of dictionary class

Create blank Set using built in function
myset=set()


print(type(myset))
#Result:<class 'set'>

Create a set with 1,2,3,4 elements
myset=(1,2,3,4)
print(myset)
#Result:(1,2,3,4)

- Set Can not Contain any mutable object such as list
Example:
my_set = {1, 2, [3, 4]}
#Result:Error :- unhashable type: 'list' 

*Accessing Items From set*
- You can not access Element refering by index becuase set are unordered and item has no index.
- You can use for loop for accessing the element as follows
Example:
myset={1,2,3,4}
for i in myset:
	print(i)
#Result 
1
2
3
4

*Check Element present in set or not*

- *in* keyword is used to check existence of an element in set
- Return True if element exists in set otherwise Return False

Example:
color={'red','green','blue'}
if('red' in color):
	print('red is present')
else:
	print('red is not found')

#Result:red is present'


*Get the set length*
color={'red','green','blue'}
length=len(color) 
print(length) 

#Result:3
