'''
Metacharacters are characters that have special meaning within regular
expressions. The period (.) ,brackets []  are  metacharacters;

To escape a special metacharacter use \ before that metacharacter

'''
import re
inputstring='''
a=[]
b=['.',1,5]
'''

#Find out the occurence of [] in input string and print
#outputstring=re.findall(r'[]',inputstring) this is the wrong solution
outputstring=re.findall(r'\[\]',inputstring)
print(outputstring)

#here [] is escaped using \  charcter as \[\] 
