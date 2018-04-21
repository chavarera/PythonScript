# Class
# to create a class you need to use class keyword
# First alphabet of class name must be capital
# class contains attributes and method
# When a object of class is created then by default __init__() method is called
# init() method is called constructor of class who will assign some memory unit to the attributes

# The first paramater of constructor is self

class Person():  # here Person is class name
    def __init__(self, name, age, gender, salary):
        # print('Init method is called')
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary


person1 = Person('rajesh', 23, 'male', 14523)
# for this object self=person1 so if we want to know the name of person1 then
print(person1.name)

person2 = Person('ragini', 22, 'female', 14690)
# self=person2
# salary of person2
print(person2.salary)
