'''Histogram is the graphical representation of numeric data distibution'''
import matplotlib.pyplot as plt #module for setup function for used for plotting
fig=plt.figure("Histogram") #this will simple give name to the histogram window
ax=fig.add_subplot(1,1,1) #in histogram window add new plotting place where our histogram will place there

''' hist contains set of data to be plotted in histogram
    bins are the number of coloumns to show
    facecolor for yello-y,red-r,green-g,blue-b
    normed 
'''
ax.hist([21,12,23,35,45,45,60,33,22,56,34,28,40,41],bins=14,orientation='vertical',facecolor='y')


plt.title('Distribution')
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show(fig)
