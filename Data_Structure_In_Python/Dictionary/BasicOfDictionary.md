____________________________

Day 12:Lecture 1
Content: Dictionary
Author:Ravishankar Chavare
Date:12-06-2019
LinkedIn:https://www.linkedin.com/in/ravishankar-chavare-84474a102
_______________________________

*Dictionary*.
- Dictionary holds *key:value* pair which unlike other data types that hold only single element.

- A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

*Keys* are unique within a dictionary while values may not be. 

*values* of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

- Key value is provided in the dictionary to make it more optimized. 

- Python Dictionary works similar to real world Dictionary when key element is uniques.


*How to Create dictionary*

Syntax:
#Create empty dictionary
dictname=dict()

#Using {} parentheses
dictname={}

#dictionary with element 
dictname={"key1":"value1","key1
2":"value2"}


Examples:
#Create empty dictionary
mydict=dict()

#Dictionary with 2 element
mydict={"name":"ravi","age":20}

#dictonary with list items
mydict={"name":"ravi","age":20, "subject":["math","English"]}
print(dict)

#Result:{"name":"ravi","age":20, "subject":["math","English"]}


*Accessing Key value from dictionary*
 - get all keys from dictionary 

Syntax:
dictname.keys()


Example
mydict={"name":"ravi","age":20, "subject":["math","English"]}
keys=mydict.keys()
print(keys)

#Result:["name","age","subject"]


 - get all values from dictionary 

Syntax:
dictname.values()


Example
mydict={"name":"ravi","age":20, "subject":["math","English"]}
Val=mydict.values()
print(Val)

#Result:["ravi",20,["math","English"]]

*Accessing specific value using key*
- Here we can access element using key instead of indexing.so position of key doesn't matter in dictionary.

There are two different method to Access element using key

1.using normal method
Syntax:
name=dictname[key]

Example:
Get *ravi* from mydict using key *name*
mydict={"name":"ravi","age":20, "subject":["math","English"]}
name=mydict["name"]
print(name)

#Result:ravi

2.Using Built in method get()
Syntax
dictname.get(keyname)


Example
mydict={"name":"ravi","age":20, "subject":["math","English"]}
name=mydict.get("name")
print(name)

#Result:ravi



*Error when you trying to Access non existence key*
Example:

mydict={"name":"ravi","age":20, "subject":["math","English"]}
#access birthdate
date=mydict["birthdate"]

#Result:Error key error 


*Using for loop access keys and values*
Example:

mydict={"name":"ravi","age":20, "subject":["math","English"]}
for key,value in mydict.items():    
            print(key,value)
#Result:
name ravi
age 20
subject ["math","English"]
