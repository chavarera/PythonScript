#String Formatting is  one good way to joins and combines two or more string with diffrent data
#for string formatting {} is used to blank space to get data from .format() .format(variabless are used)

a=10
b=20
c=39

#1.String Formatting
#for example if we want to write a value is 10 then normal way to write is
print('a value is '+str(a))


#using String Formatting
print('a value is {}'.format(a))


#if we want to print a value is 10 and b value is 20 and c value is 39
#normal way
print('a value is '+str(a)+' and b value is '+str(b)+' and c value is '+str(c))

#using string Formatting
print('a value is {} and b value is {} and c value is {}'.format(a,b,c))


#You can also give position inside {} block like {1} then this will get value from .format(0position,1position,2postion)
print('a value is {2} and b value is {1} and cvalue is {0}'.format(a,b,c))
#here {2} get value from format and get value whose position is 2 in formatting



#2.Type Conversion

#Type conversion int to float
#foolowing example showing int to float
print('a value is {0:f}'.format(a))


#for 2 digit
print('a value is {0:.2f}'.format(a))



#type conversion double to flot
#bydefault in python the dataatype is double for calculation
print('2/3 answer is {}'.format(2/3))

#to convert into float
print('2/3 answer is {0:f}'.format(2/3))




#3.#spacing using 'd'
#this is used for giving spacing to integer
print('answer is {0:3d}'.format(2))
#here the element is 1 digit and we give space for 3 digit means only 2 digit space show


#for string we use left chevorn(<) and right chevorn(>) for giving space
print('my name is {}'.format('abhi'))

#to give space before name we use right chevorn
print('my name is {0:>8}'.format('abhi'))


#to give space after name we use right chevorn
print('my name is {0:<8} ....'.format('abhi'))



#4.text at center of Astric (*)
print('{0:*^11s}'.format('rahul'))

#this will create 11 * but rahul string is 5 chacter so 6 astric(*) will be printed 3 left side and 3 right side if 7 star there then 4 at right side and 3 at left side



#5.String Formatting inside a loop
for i in range(1,11):
    print('{0:5d}{1:5d}{2:5d}'.format(i,i**2,i**3))