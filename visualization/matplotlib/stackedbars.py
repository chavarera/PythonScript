import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy

#stacked bar data
bar1=[2,1,4,5]
bar2=[1,1,4,3]
bar3=[3,2,4,5]
bar_width=0.5

#list of element from 0 to rang(bardata)
x=numpy.arange(len(bar1)) #to create a list of how much element in bar1 you can take any bar

#plot the bar
'''
x=list of 0 to range(bar)
bar1=bar1 data
color=Your prefered color
width=you can set any width of the bar
bottom for first data no need
for second data you need to pplace bar on first data so bottom=bar1
for third data you need to place bar on bar1+bar2 data so create list and it
'''
plt.bar(x,bar1,color='black',width=bar_width)
plt.bar(x,bar2,color='gray',bottom=bar1,width=bar_width)
plt.bar(x,bar3,color='lightgray',bottom=[x+y for x,y in zip(bar1,bar2)],width=bar_width)

#add  x info and yinfo
plt.xticks(x,['one','two','three','four'])# This place label to x axis
plt.yticks(numpy.arange(17)) #create y axis to 0 to 16 range
plt.grid() #place grid lines if you want to place on y axis just add plt.grid(axis='y')

#legend info block
lightgray=mpatches.Patch(color='lightgray',label='bar3')
gray=mpatches.Patch(color='gray',label='bar2')
black=mpatches.Patch(color='black',label='bar1')
plt.legend(handles=[lightgray,gray,black],loc='upper left')


#this is the title,xlabel,ylabel of stacked bar
plt.title('Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


