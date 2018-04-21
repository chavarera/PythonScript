# every class has one method __init__() which is automatically called when the class object is created

# every class method need one parameter that is self or you can write your classname intead of self

# 1.using Self keywords
class Person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def isegl(self):  # this is new method defination
        if self.age >= 18:
            return True
        else:
            return False


person1 = Person('Abhi', 17, 3333)
print(person1.isegl())  # calling method using instance of class means object of class


# 2.using Class name
class Person2():
    def __init__(Person2, name, age, salary):
        Person2.name = name
        Person2.age = age
        Person2.salary = salary

    def isegl(Person2):  # this is new method defination
        if Person2.age >= 18:
            return True
        else:
            return False


person1 = Person('Abhi', 19, 3333)
print(person1.isegl())  # calling method using instance of class means object of class

