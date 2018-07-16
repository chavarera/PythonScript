'''
Use of search method in Regular expression

1:single First match
    re.search() to find the first match for a pattern.

2:Multiple Match
     findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.

'''

import re #import re module


#input data
inputstring='''
Hello i am Chavare Ravishakar  working as data Engineeer .
I am 18 year Old and my email id is ravisha.nkarc@t-outlook.biz
and personal email is demo@email.com, testdemo@gmail.com,charm565@gmail.com 4gamd@dfhj3.com
'''



#Simple Search the First occurence of an given pattern 
match=re.search(r'[\w.-]+@[\w.-]+',inputstring)
print('**Using re.search() **')
if match:
    print(match.group())
else:
    print('No match Found')




#To Find multiple Occurence of given pattern use re.findall()
'''findall() is probably the single most powerful function in the re module'''
print('\n** Using re.findall() **')

emails=re.findall(r'[\w.-]+@[\w.-]+',inputstring)
for e in emails:
    print(e)



'''
Output:-

**Using Search **
ravisha.nkarc@t-outlook.biz

** Using re.findall() **
ravisha.nkarc@t-outlook.biz
demo@email.com
testdemo@gmail.com
charm565@gmail.com
4gamd@dfhj3.com
'''
