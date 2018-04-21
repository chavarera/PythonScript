# multilevel inheritance
# In multiple inheritance, the features of all the base classes are inherited into the derived class.
# We can inherit a derived class from another derived class, this process is known as multilevel inheritance

# base class for GamingLaptop
class Laptop():  # base class/parent class
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


# this is derived class from Laptop
# this is Base class for SuperGamingLaptop
class GamingLaptop(Laptop):  # derived class /sub class
    def __init__(self, brand, screen, hdd, ram, graphics, cpuspeed):
        super().__init__(brand, screen, hdd,
                         ram)  # call parent class method __init__() to define brand,screen,hdd,ram from base class or parent class Laptop
        # now define remaining attributes here
        self.graphics = graphics
        self.cpuspeed = cpuspeed

    def data(self):
        print('data is for Gaming laptop')


# this is derived class from GamingLaptop
class SuperGamingLaptop(GamingLaptop):
    def __init__(self, brand, screen, hdd, ram, graphics, cpuspeed, processor):
        super().__init__(brand, screen, hdd, ram, graphics, cpuspeed)
        self.processor = processor


lenovogaming = SuperGamingLaptop('Lenovo', 15.6, 1, 8, 4, '3.0ghz', 'I7')
lenovogaming.showinfo()  # when we call this method first it find in SupergamingLaptop class if it not found then search it in GamingLaptop class is also that method not found then it will find out that method in laptop And run from ther

lenovogaming.data()  # this method run from GamingLaptop Class
