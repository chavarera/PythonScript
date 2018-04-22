#To findout postion of word or charcter from given string or paragraph use find operator

mystring="i love to play cricket and football"
print(mystring.find("o"))
#3

print(mystring.find("cric"))
#15


#if we want to print string from play to onwards then
startingindex=(mystring.find("play"))
print(mystring[startingindex:])
#play cricket and football



#if we searching a not character or word in a paragraph which is not present in that paragraph or string then result of find operator will be -1
print (mystring.find("hahaha"))
#-1


#if we want to findout second occurance of of required string
first=(mystring.find("o"))
second=(mystring.find("o",first+1))
print(second)
