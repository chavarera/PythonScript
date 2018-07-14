'''
Regular expressions are case sensitive
so [A-Z] will give result from uppercase A-Z letter
[a-z] will give result from lowercase letter a-z

'''
import re
mystring=" my name is ravi visit my website https://protutr.com"

#Matching Simple Text
output=re.findall(r'my',mystring)
print(output)

# this will just serach simple 'my' text inside the input string and give output
#output:['my', 'my']


#Matching A Character
'''Multiple . s may be used, either together (one after the other—using ..
will match any two characters next to each other) or in different locations
in the pattern'''

mytext='''
abc1.txt
abcd.txt
abc2.txt
ax.txt
abc.txt
antk.txt
tbc.txt
abc3.txt
'''

'''find all text starting with abc and followed by another character'''
outputdata=re.findall(r'abc.',mytext)
print(outputdata)
#output ['abc1', 'abcd', 'abc2','abc.', 'abc3']
# . matches any character, alphabetic characters, digits, and even . itself:
#if you want to find out all text preceding any character and followed any charcter and in this middle b
print(re.findall(r'.b.',mytext)) #output ['abc', 'abc', 'abc', 'abc', 'tbc', 'abc']


