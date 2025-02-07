#dunders(MAgical Functions)
"""  dunder is a shorthand for double underscore, and it refers to special methods or attributes that are surrounded by double underscores on both sides """
#__init and teh __del__ dunder
class Parson:
    #__init__ it a contructor method for the class and  It is called when an instance of the class is created.
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #__del__
    def __del__(self):
        print("The object is bieng deconstructed")

    #__str__ this method is used to print a string nice representation of an object, its called by the pring and str() built in function.
    def __str__(self):
        return f"MyClass with value: {self.name}"
    #__repr__ method is called by the repr() built-in function to compute the "official" string representation of an object. This is typically used for debugging.
    def __repr__(self):
        return f"MyClass({self.name}: {self.age})"
p= Parson("Mike",24)
print(p)#MyClass with value: Mike
print(repr(p))#MyClass(Mike: 24)