#To write simple Document inside a program

#we can write document using '''document or help add here''' inside
#1.class
#2.Normal Function
#3.Methods


#To fetch the our written code document we have two different method to collect documents
#1.__doc__
#2.help() function


#1.__doc__
#Doc string is used to get detail information about code
#Simple syntax of __doc__ for class is : Classname.__doc__
#               __doc__ for class method:Classname.methodname.__doc__
#               __doc__ for simple normal function:FunctionName.__doc__


#2.help() function
#help() function is used to retrive all document related to class unctions and method
#we can simple define help as :help(any class,function object)
#help give all document about
#1.about class and
#2.defined method inside of class
#3.dictionaries

def CustomFunction():
    '''I am a simple custom function'''#document about function
    print('i am from custom function')
class Circle():
    '''this is Circle Class used to find out area''' #Add Document About Class here
    def __init__(self,radious,pi):
        self.radious=radious
        self.pi=pi
    def area(self):
        '''this is area method inside Circle ''' #document inside a method
        return self.pi*self.radious**2
circle1=Circle(3,3.14)
print(circle1.area())

#TO print out Class Document
print(Circle.__doc__)


#To print out method documnet from class
print(Circle.area.__doc__)


##To print out simple function Document
print(CustomFunction.__doc__)


#To printout all document of class then we can use help function
help(Circle)


#to printout all data about predefined objects
help(list)
