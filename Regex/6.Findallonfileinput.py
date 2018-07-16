'''
For file you need to habbit to itterate all data through loop  and call findall() method from loop
or easist way

Instead, let findall() do the iteration for you -- much better!
Just feed the whole file text into findall()
and let it return a list of all the matches in a single step
'''

import re
import os
readfile=open('inputfile.txt','r')
emails=re.findall(r'[\w.-]+@[\w.-]+',readfile.read())
for e in emails:
    print(e)
