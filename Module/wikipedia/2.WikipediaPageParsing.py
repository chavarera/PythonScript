'''
created by:Ravishankar Chavare

We alredy Learn Basic of wikipedia keywords and short description now we are here to learn the full
page parsing of wikipedia
'''
import wikipedia 

#To get full page details and data use wikipedia.page("keyword")

simple_page=wikipedia.page("India");

#now simple_page is wikipedia object you can extact data from it

#1.Get The Title Of page
title=simple_page.title
print("Title of Page: ",title)


#2.Get The url of wikipedia Page
url=simple_page.url
print("url of searched page : ",url)


#3.To Get the Content Of Page
content=simple_page.content
print("Content: ",content)


#4.To Get the Image of page

image_url=simple_page.images  #This will Collect All Images url into list

#To print simple first image url You can use
print("First Image Url:",image_url[0])



'''
To change the language of the Wikipedia you are accessing,
use wikipedia.set_lang. Remember to search
for page titles in the language that you have set, not English!:
'''

#To set Language as english
wikipedia.set_lang("en")
print(wikipedia.summary("india"))


#To Get Available languages list
languages=wikipedia.languages()

#To Check That Language is avilable in wikipedia or not
print('en' in wikipedia.languages()) #this will give true or false 




'''
for more tutorial Visit
https://wikipedia.readthedocs.io/en/latest/quickstart.html

'''

