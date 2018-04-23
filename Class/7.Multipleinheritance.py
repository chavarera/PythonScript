# One class extending more than one class is called multiple inheritance.

#parent class 1
class A:
    def __init__(self):
        print('i am from Class A')
        self.name = 'John'
        self.age = 23

    def getName(self):
        return self.name

#parent class 2
class B:
    def __init__(self):
        print('i am from Class B')
        self.name = 'Richard'
        self.id = '32'

    def getName(self):
        return self.name


class C(B,A):  #extend two base class
    print('i am from Class c')
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def getName(self):
        return self.name


C1 = C()
print(C1.getName())


#When You called c Class then __init__method of c is fist called after calling c class inside init() method
#then class A is called because in C class Initilization we called A class initilization  first
#then Class B is called


#firstly name value=jhon
#After calling to B class name value is override with jhon

#So the Final Output is Richard