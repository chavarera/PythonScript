#Following are the some string methods

##1.Split
#if you want to devide a string with white space or commas or some special charcter then split method is used
mystring="india pakistan china america"


#split a string with whitespaces
splitstring=mystring.split(' ')
print(splitstring)
##['india', 'pakistan', 'china', 'america']

##if you want to split that string and store it in different variable
a,b,c,d=mystring.split(' ')
print(a)
print(b)
print(c)
print(d)

##india
##pakistan
##china
##america


##2.join
mylist=['india', 'pakistan', 'china', 'america']
strings=','.join(mylist)
print(strings)
##india,pakistan,china,america




##3.count
lis=[3,5,54,3,3,3,4,5,56,66,3,3,3,23,4,6,6,77,34,345,67,6,78]
#if you want to count how much times the 3 appears in list
print(lis.count(3))
##7




##4.Replace
stat='kat is good girl'
##if you want to replace is with was then replace is used
#replace('old word','new word')
newstring=stat.replace('is','was')
print(newstring)

##kat was good girl

