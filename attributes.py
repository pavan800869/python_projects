 
class Children:
    def __init__(self, name, **kwargs) -> None:
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def __str__(self) -> str:
        return "{}: {}".format(self.__class__.__name__, self.name)

# All these classes are seperated in different files and imported to one and ran together.
class Thief(Children):
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
        # super uses to search anything in father class of inheritence. 
        super().__init__(name, **kwargs)
        self.name = name
        self.sneaky = sneaky 
        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
        
# Self must be used in defining oops functions in python.
    def hide(self, light_level):
        return self.sneaky and light_level == 10
# "Self" and "light_level" are two parameters of the functions.
# DRY ==> Don't repeat yourself. 
# To organise codes in an order there is a menthod called MRO ==> Method resolution order.
# We can make codes in different files and import them again ,help of import and add then to the main class. Then we can create another file and import that main class and we can run all the code at once which is shorter easier and more efficient at finding errors.
