from itertools import *
from operator import itemgetter

#Your List
a=[2,3,4,7,8,10]

for k, g in groupby(enumerate(a), lambda (i,x):i-x):
 datas=map(itemgetter(1), g)
 #Spplitted Lists
 print(datas)

'''
Output
[2, 3, 4]
[7, 8]
[10]
'''
