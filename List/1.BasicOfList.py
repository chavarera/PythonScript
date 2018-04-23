'''When you create a list in Python, the interpreter creates an array-like data
structure in memory to hold your data, with your data items stacked from
the bottom up'''

'''To define  a List'''
country=['india','america','japan','china']
'''
postion element
0   india
1   america
2   japan
3   china
'''

'''To printing a list'''
print(country)


'''To Get Length of List'''
print(len(country))


'''Prining list element by using indexing'''
print(country[0])

'''printing last element from list'''
print(country[-1])

'''Assigning new element in list ,replacing'''
country[1]='Nepal'
print(country)


'''Capitlize the first letter'''
print(country[1].capitalize())

'''To lowercase conversion'''
print(country[1].lower())

'''To swapecase'''
print(country[1].swapcase())

'''Apend And Insert Into List'''

'''appending element to last to list'''
country.append('america')
print(country)

'''How to Add element in list at any postion use insert() method'''
#listname.insert(postion,'element')
country.insert(1,'UK')
print(country)
#['india', 'UK', 'Nepal', 'japan', 'china', 'america']


#If you want to add elemnt at last position and you tried to add element at -1 postion
#country.insert(-1,'oman') now in our last updated list america is at -1 position if you run
#such query then america will shift to right and oman addedd at location of the america
country.insert(-1,'oman')
print(country)
#['india', 'UK', 'Nepal', 'japan', 'china', 'oman', 'america']


#if you give position out of range of list then the element is added at last postion
country.insert(4543,'Bhutan')
# print(country[4543]) this will give an error
print(country)
#['india', 'UK', 'Nepal', 'japan', 'china', 'oman', 'america', 'Bhutan']


#if you used negative number which is out of range then that item will place at zero postion
country.insert(-34,'SA')
print(country)
#['SA', 'india', 'UK', 'Nepal', 'japan', 'china', 'oman', 'america', 'Bhutan']



#deleting element from list
#----------------------------------------
#if you removed item using del statment you cant use them for further process

#1.deleting element using indexing
#del listname[index]
del country[1]
print(country)

#['SA', 'UK', 'Nepal', 'japan', 'china', 'oman', 'america', 'Bhutan']



#2.You can use pop method to remove element from list and use it whne you need it
country.pop() # this line remove the last elment from the given list
print(country)
y=country.pop() # this line save them removed element
print(country)
print(y)


#removing element from list at specific posiotion
country.pop(3)
print(country)


#3.Removing element using remove method
#using remove method you can easily remove element using list item
country.remove('SA')
print(country)

#If you give a such item name which is not present in the list it will give error
 #country.remove('jkdsncfsd')  jkdsncfsd element is not present in list



#How to findout position or index of given string
index=country.index('Nepal')
print(index)

#print(country.index('nepal')) this data searches in case sensetive manner



#How to reverse elemnt from given list
country.reverse()
print(country)


#Sort the list alphabetically
country.sort()
print(country)

#['Nepal', 'UK', 'china', 'oman'] Capital aplbhabets first


#sort the list into reverse order
country.sort(reverse=True)
print(country)

#['oman', 'china', 'UK', 'Nepal']



#Sorted Function
#after sorting we cant go back on original list so we use sorting function
#if you want to sort in alphabetical order
print(sorted(country))

#For ReverseSorting
r=(sorted(country))
r.reverse()
print(r)







#List in List
x=[['abc','bnk'],'cds','dss']
print(x[0][1])
#bnk
print(x[1][1])
#d




#Converting any data to list data type
y=('Ravishankar')
mylist=(list(y))
#['R', 'a', 'v', 'i', 's', 'h', 'a', 'n', 'k', 'a', 'r']
print(mylist[1])
#a