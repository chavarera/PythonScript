'''In regular expressions a set of
characters is defined using the metacharacters [ and ]. [ and ] define a
character set, everything between them is part of the set, and any one of
the set members must match (but not all)
'''
import re
inputstring='''
abc1.txt
abcd.txt
abc2.txt
abc3.txt
ca1.xls
na1.xls
na2.xls
sa1.xls
ca1.xls
'''

#Find out text whose name start with n or c and followed by 'a' followed by any character
#and then .xls
outputstring=re.findall(r'[nc]a..xls',inputstring)
print(outputstring)

#output :['ca1.xls', 'na1.xls', 'na2.xls', 'ca1.xls']
'''
Describing ["nc]a..xls"  Regular Expression

[nc] start with n or c
a    second letter must be a
.    third letter anything
.    fourth letter also anything
xls  and then xls 

'''




#Example 2 Findout output string using character set range
output=re.findall(r'[nc]a[0-1].xls',inputstring)
print(output)
#output :['ca1.xls', 'na1.xls', 'ca1.xls']
'''
[0-1] this is charcter set range from 0 to 1 you can specify it according to your need
'''
