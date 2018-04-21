# Inheritance
# inheritance means creating a new class who access variables and methods from parent class
# A class can inherit attributes and behaviour methods from another class, called the superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class

# simple Example
# laptop -has atrributes brand,screen,hdd,ram,
# gaming laptop-has attributes brand,screen ,hdd,ram,graphicscard,processing clock speed


# You can derive initailization from parent class in two way
# 1. super().__init__(Variable from parent claas)
# 2.Classname.__init__(self,Variable from parent claas)

# Now First Create a Class for normal Laptop

# this is base class/parent class
class Laptop():
    def __init__(self, brand, screen, hdd, ram):
        self.screen = screen
        self.ram = ram
        self.brand = brand
        self.hdd = hdd

    def showinfo(self):
        print('The laptop brand is {} whose screen size is {}. And who has  {} TB hdd and {} gb ram'.format(self.brand,
                                                                                                            self.screen,
                                                                                                            self.hdd,
                                                                                                            self.ram))

    def data(self):
        print('data is for normal laptop')


# Now Create Another class for GamingLaptop
# but gaming laptop has some attributes which are already present in laptop class
# so create new class with name GamingLaptop which inherits laptop class inside it

# this is derived class
class GamingLaptop(Laptop):  # add parent class name inside bracket
    def __init__(self, brand, screen, hdd, ram, graphics, cpuspeed):
        super().__init__(brand, screen, hdd,
                         ram)  # call parent class method __init__() to define brand,screen,hdd,ram from base class or parent class Laptop
        # now define remaining attributes here

        self.graphics = graphics
        self.cpuspeed = cpuspeed

    def data(self):
        print('data is for Gaming laptop')


# Now create a object of derived class and call method from parent class
lenovogaming = GamingLaptop('Lenovo', 15.6, 1, 8, 4, '3.0ghz')
lenovogaming.showinfo()

# method overriding
# derived class has a same name method as compare to parent class then only derived class methood is called
# both class has same method data()
lenovogaming.data()  # this will call method of GamingLaptop Class


