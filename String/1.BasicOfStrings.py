#Strings
#String is collection of Alphabets numbers and special charcter
#following are the some defualt string function
stringname=("kjdsfndnfd")

#stringname[1] gives j string started counting first charter as 0 second as 1 third as 2 in this way
print(stringname[1])
#j


#stringname[-10] gives k that counts from last character and search like d at -1, f at -2,-3...
print(stringname[-10])
#k


#selecting sub sequences from string
#Syantax variablename[starting position:endingposition + 1]
# for example if you want to print sfn from above stringname then where s is at starting position is 3 and n endpostion is 5 add 1 in it then total is 6
print(stringname[3:6])
#sfn


#stringnam[10] gives error index out of range
#print(stringname[10])


#you can use : for multiple use like
# variablename[startingpostion:]   in this example if we just add starting postion then then resultant substring contains output from statring postion to last charcter
print(stringname[6:])
#dnfd



#variablename[:ending postion ] this will give output in such manner from starting to that ending position
print(stringname[:4])
#kjds

#variablename[:] this will give who string as output
print(stringname[:])
#kjdsfndnfd


#IMP NOTE
#if you provide out of range  ending index it doesent give error it will print full string
print(stringname[:50])
#kjdsfndnfd

#if you provide out of range  starting index it doesent give error it will print full string
print(stringname[-100:])
#kjdsfndnfd
