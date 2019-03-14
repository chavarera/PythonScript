'''
Dictionary:
-Dictionary holds key:value pair which unlike other data types that   hold only single element 
-Key value is provided in the dictionary to make it more optimized.
-Python Dictionary works similar to real world Dictionary when key element is uniques
'''


#create Simple Dictionary
blankdict=dict()


#Dict with element
elemntdict={'name':'jhon','roll':20,'college':'MIT'}

#simple print dict
print(elementdict)


#-----------------------------------------------------------------------------------------
#                     Accessing Values and keys From dictionary
#-----------------------------------------------------------------------------------------

#print name from dictionary
name=elemntdict['name']
print(name)

#Accessing Only keys from dictionary
keys=elemntdict.keys()
print(key)

#Accessing Values Only
vals=elemntdict.values()
print(vals)

#useing For Loop iterate the dictionary

for key,value in elemntdict.items():
    print(key,value)
