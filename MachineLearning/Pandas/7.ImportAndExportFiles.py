##--------------------------------
##Created By:Ravishankar Chavare
##version:python 3.7
##Date:11/03/19
##File_des:Reading a Data File And Exporting it into RequiredFormat
##--------------------------------

#-----------------------------------IMPORT Packages---------------------------------------------------
import pandas as pd #import Pandas

'''
Using Pandas You can import variety of data files for analysing or manipulation you can use same for exporting
dataframes to different Forms
read_clipboard
read_csv
read_excel
read_feather
read_fwf
read_gbq
read_hdf
read_html
read_json
read_msgpack
read_parquet
read_pickle
read_sas
read_sql
read_sql_query
read_sql_table
read_stata
read_table

'''
#You can Get the list of data files or structures  supoorting by pandas for import and Export using follwing simple Example
formats=[val for val in dir(pd) if 'read' in val]
print(formats)


#For Reading files or datastructur simple use pd.read_datastructure(path)


#for Reading csv File
csvfile=pd.read_csv("zipcodes.csv")


#Now Export the File into html
csvfile.to_html("zipcodesoutputfile.html")
