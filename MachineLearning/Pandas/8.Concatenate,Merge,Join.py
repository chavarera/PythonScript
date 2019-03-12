##--------------------------------------------------------------------------------------------
##Created By:Ravishankar Chavare
##version:python 3.7
##Date:12/03/19
##File_des:Merge, Join, & Concatenate
##--------------------------------------------------------------------------------------------

#-----------------------------------IMPORT Packages---------------------------------------------------
import pandas as pd #import Pandas

#Define two diffrent list using list comprehension
list1=[i+3 for i in range(11)]
list2=[i+1 for i in range(11)]

#Create Two dataframe
df1=pd.DataFrame(list1,columns=['FirstList'])
df2=pd.DataFrame(list2,columns=["FirstList"])

#------------------------------------------------------------------------------------------
#                                   1.Concatenate
#------------------------------------------------------------------------------------------
'''
1.Concatenate

simple appending the another dataframe (up,down,left,right)

How to use Axis parameter while concatenating

If your dataframe have same column name then this will append data to up and down manner by defualtly or you can specify axis=0
    Example1:pd.concat([df1,df2],axis=0)

if you want to concatenate data with left or right appending then use axis=1
```Example1:pd.concat([df1,df2],axis=1)

for simple concatenating the dataframe use(concat()) method
syntax:
'''
#normal Same Columns Data Conactenate(up and down just switch the data frame postion)
concatdf1=pd.concat([df1,df2]) #you can also use pd.concat([df1,df2],axis=0)
print(concatdf1)

#for left and right concatenation just provide axis=1
concatdf2=pd.concat([df1,df2],axis=1)
print(concatdf2)


#If You Have Some different column then
df2.columns=['SecondList'] #Change the column name of second dataframe to Secondlist

differentconcatenate=pd.concat([df1,df2])#this will do left and right concatenation and assign NaN to a missing value
print(differentconcatenate)


#------------------------------------------------------------------------------------------
#                                   2.Merging
#------------------------------------------------------------------------------------------

'''
merging are used to combine the dataset depending upon the columns value based on the key columns
    Syntax:
        pd.merge(df1,df2,on="keyname")

you can use how parameter for inner,outer,left,right merging
if you have two dataframe and used leftmerge then all rows from left table a it is and if a row not found in right table then 
NaN is added to the data cell
    
    Syntax:
        pd.merge(df1,df2,how='outer')
    

'''
firstlist=[i*2 for i in range(10)]
secondlist=[i*3 for i in range(10)]
key=[i+1 for i in range(10)]

#Creating dataframe with two different columns
mdf1=pd.DataFrame({'key':key,'value':firstlist})
mdf2=pd.DataFrame({'key':key,'value':secondlist})

merged_df=pd.merge(mdf1,mdf2,on="key")
print(merged_df)

#Note :If specified Key is not present then it will return blank index values only


#------------------------------------------------------------------------------------------
#                                   3.join
#------------------------------------------------------------------------------------------
'''
Join is just simple Variation of normal merge
 we can use how parameter for inner,outer,left,right
 lsufix append the string at end of columns name
 similar to lsufix rsufix used to append the string to right side dataframe columns name
'''

#Consider the above mdf1 and mdf2 dataframe
mdf1.set_index("key")
mdf2.set_index("key")
joined_df1=mdf1.join(mdf2,lsuffix='_x',rsuffix='_y')
print(joined_df1)
