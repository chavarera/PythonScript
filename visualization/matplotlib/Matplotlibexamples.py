import matplotlib.pyplot as plt

'''Histogram'''
fig=plt.figure("Histogram example")
ax=fig.add_subplot(1,1,1)
ax.hist([21,21,2,44,2,2,3,4,1,3,23,23,2],bins=7)
plt.title('Title of histogram')
plt.xlabel('x data')
plt.ylabel('y data')
plt.show()

'''Box Plot'''

fig2=plt.figure("Another Box Plot example")

ax=fig2.add_subplot(1,1,1)
data=[21,21,2,4,2,2,3,4,1,3,23,23,2]
ax.boxplot(data)
plt.show()

'''Bars'''
fig3=plt.figure('Bar Example')
ax2=fig3.add_subplot(1,1,1)
ax2.set_ylabel('Y')
ax2.set_xlabel('X')
ax2.set_title('Bars Title')
ax2.bar([1,2,3,4],[5,10,4,9],[0.5,0.5,0.5,0.5],color=['r','b','g'])
plt.show()

'''bar Lines'''
fig4=plt.figure('Linebars')
ax4=fig4.add_subplot(1,1,1)
ax4.set_xlim([0,12])
ax4.set_ylim([0,12])
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_title('Lines')
ax4.plot([1,2,4,7,8],[5,2,3,4,3],'r')
plt.show()
