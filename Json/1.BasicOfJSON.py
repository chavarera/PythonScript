## JSON Stands For JavaScript Object Notation or JSON is an open-standard file format
## that uses human-readable text to transmit data objects
## consisting of attribute–value pairs and array data types.

'''Json is Light weight format as compared to XML'''


import json #this is python bydefault module need to import

#json can be store any dictionaries or list item
data="{name:ravi,number:12345678}"

#this will simple get data from data variable and save it in demo.json
with open('demo.json','w') as json_file:
    json.dump(data,json_file)

##Python has great JSON support, with the json library.
##can convert lists and dictionaries to JSON,
##and convert strings to lists and dictionaries.
##JSON data looks much like a dictionary would in Python,
##with keys and values stored
