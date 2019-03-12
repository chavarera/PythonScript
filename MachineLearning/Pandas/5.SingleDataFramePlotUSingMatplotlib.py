##--------------------------------
##Created By:Ravishankar Chavare
##version:python 3.7
##Date:11/03/19
##File_des:Simple DataFrame Plotting
##--------------------------------

#-----------------------------------IMPORT Packages---------------------------------------------------
import pandas as pd #import Pandas
import matplotlib.pyplot as plt #For Ploting the Plot
from matplotlib import style #assiging the Style to plot


#Here use any Style Format which are alredy designed
#for Custom style visit here https://matplotlib.org/users/style_sheets.html
style.use("ggplot")


#Simple Data Frame Create
df=pd.DataFrame({'day':[1,2,3,4,5],'visitor':[200,230,100,210,250],'BounceRate':[10,28,1,2,4]})

#Set Index as Day
df.set_index("day",inplace=True)


#Now plot the Datframe using datframe.plot()
df.plot()

#Set the title to plotted Graph
plt.title("VisitorCount")

#Now Show The plot using plt.show()
plt.show()

