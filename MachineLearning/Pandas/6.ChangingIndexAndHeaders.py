##--------------------------------
##Created By:Ravishankar Chavare
##version:python 3.7
##Date:11/03/19
##File_des:Changing Index and Header (DataFrame)
##--------------------------------

#-----------------------------------IMPORT Packages---------------------------------------------------
import pandas as pd #import Pandas

#Simple Data Frame Create
df=pd.DataFrame({'day':[1,2,3,4,5],'visitor':[200,230,100,210,250],'BounceRate':[10,28,1,2,4]})

#To Changing Index just use df.set_index("keyName",inplace=True)
df.set_index("day",inplace=True)

#To Change The Header rename visitor header with Users
df=df.rename(columns={"visitor":"Users"})

#Now Print The Simple Changed Index and Headers
print(df)
