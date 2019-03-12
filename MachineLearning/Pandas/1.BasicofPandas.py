'''
https://www.listendata.com/2017/12/python-pandas-tutorial.html

What is Pandas:
Pandas Module is commonly used for data manipulation and data anlysis purpose.
It is a very powerful and versatile package which makes data cleaning
and wrangling much easier and pleasant.

Why Pandas:
-Reading Data from diffrent sources like csv,xlsx,Databases and Others
-pandas is an open source, BSD-licensed library providing high-performance, easy-to-
use data structures and data analysis tools for the Python programming language.
-iterate over the rows of datasets
-Exporting Data to CSV or Excel Format
-Easy handling of missing data
-Flexible reshaping and pivoting of data sets

What type of data can be handled using pandas:
-Tabular data with heterogeneously-typed columns
-ordered and unordered
-Any other form of observational / statistical data sets

Installing Pandas:
using pip
Open Command Prompt and type
>pip install pandas

wait some time to get install pandas in your system


Importing Pandas:
import pandas as pd
'''
#importing pandas
import pandas as pd


#importing Dataset from csv
data=pd.read_csv('users.csv')


#Get Coloumns name
print(data.columns)

'''get first 2 Coloumns name'''
print(data.columns[:2]) #indexing in python start from 0


#varibale Type in pandas data
'''To Know the Variable Type
object-string or character
int64-numeric values without decimals
'''
print(data.dtypes)#object
print(data['ZIP'].dtypes)#int64

#changes the variable type of an object
data['ZIP']=data['ZIP'].astype(float)
print(data['ZIP'].dtypes)   #float

#To get the no of rows and coloumns
print(data.shape)#(3,15)


#To views 5 rows
'''
By default head( ) shows first 5 rows.
If we want to see a specific number of rows we can mention it in the parenthesis like data.head(5) shows 5 rows data.
Similarly tail( ) function shows last 5 rows by default.
'''
print(data.head())#return 5  rows from starting
print(data.head(2))#return 2 rows from starting
print(data.tail())#return 5 rows from ending
print(data.tail(2))#return 2 rows from ending



 

