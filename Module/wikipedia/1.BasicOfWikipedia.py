'''
created by:Ravishankar Chavare

To install wikipedia use pypi open command prompt and type

pip install wikipedia


To import into python program use

import wikipedia
'''

import wikipedia


#To search a simple query on wikipedia
#use wikipedia.search("keyword")

searched_data=wikipedia.search("India")

print(searched_data)
'''
output according to keyword
['India', 'Irreligion in India', 'East India Company', 'Constitution of India',
'Government of India', 'Christianity in India', 'Savdhaan India', 'Star India',
'States and union territories of India', 'Retailing in India']
'''


#get fewer or more results by using the results kwarg:
#Example wikipedia.search("keyword", results=count)

print(wikipedia.search("India",results=3))


#To get the short description of keyword use summary method like
#wikipedia.summary("keyword")

info_india=wikipedia.summary("india")
print(info_india)





#Some Basic Exception Handeling IF You searched a keyword which is not available
#then it will generate exception with some suggested keyword use wikipedia.exceptions.DisambiguationError exceptions for getting options
try:
    mercury=wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
    ask_user=str(input("Given keyword not found we found some keyword regarding your search do you want y/n"))
    
    if(ask_user=='y'):
        print(len(e.options));
        print(e.options)
    



