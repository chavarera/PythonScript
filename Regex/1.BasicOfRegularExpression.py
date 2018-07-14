'''
A regular expression is a special sequence of
characters that helps you match or find other strings
or sets of strings, using a specialized syntax
held in a pattern. Regular expressions are widely used in UNIX world.
'''

'''
IDENTIFIRES:-

\d any number
\D anytrhing except a number

\s space
\S anything except a space

\w any charcter
\W anything except a character

. any character but except new line
\b white space arround wprds
\. a period



MODIFIRES:-

{2,6} describing about numbers expecting result 2-6
+ Match 1 or More
? Match 0 or 1
* Match 0 or more
$ Match the end of string
^ Matching the begining of string
| either or (Example {1,3} | {6-9})
[] range or variance example [1-5],[A-Z]
{x} expecting "x" amount


White Spaces
\n new line
\t tab
\e escape
\s space
\f from feed
\r return


Note:
We can use diffrent solution for solving same problem
'''


import re #importing regular expression module


mystring='''
hi Akash is 67 years old,
and  Ajay is 28 years old, Raj is 109'''

#find ages
'''
re is module name
findall is method
r is for regular expression
\d finding digit
{1,3} modifier to find 1 or 2 or 3 digit number
'''
ages=re.findall(r'\d{1,3}',mystring)
print(ages)

# this will give output : ['67', '28', '109']


# Now Find out name
names=re.findall(r'[A-Z][a-z]*',mystring)
print(names)

#this will give output :['Akash', 'Ajay', 'Raj']


# save this output in dictonary
mydict={}
index=0
for name in names:
    mydict[name]=ages[index]
    index=index+1
print(mydict)
