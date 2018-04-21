
#there are two TYPE Of Variables
#1.instance variable-defined in __init__() method
#2.Class Varaible-defined in class

#Static(Class) variables and instance variables both are member variables because they are both associated with a specific class

#Instance Variable
#Instance variables are not shared between the objects of a class. Each instance will have their own copy of instance variables
#every object has it's own personal copy of an instance.
#to call instance variable we need to self.varaiblename
#Instance variables can be accessed only through object reference


#Class Varaible
#Class variables only have one copy that is shared by all the different objects of a class
#Class variables are common to all instances of a class. These variables are shared between the objects of a class
#to call Class variable we need to classname.varaiblename
#Class variables can be accessed using either class name or object reference.



#Example of instance variable
class Circle():
    def __init__(self,radious,pi):
        self.radious=radious
        self.pi=pi      #instance variable
    def area(self):
        return self.pi*self.radious**2
circle1=Circle(3,3.14)  #we are sending instance varaible
print(circle1.area())



#Example of Class variable

class Circlec():
    pi=3.14    #this is called class variable we are defining here
    def __init__(self,radious):
        self.radious=radious
    def area(self):
        return Circlec.pi*self.radious**2 #Here we called class variable
circlec=Circlec(3)
print(circlec.area())
