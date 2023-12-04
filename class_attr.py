
def twofold(x):
    return x*2

class CCM:
    '''This is a doc string given in the class '''
    def __init__(self, v):
        self.v = v
        
    def __display(self):
        print(f"The current value of 'V' is {self.v}")
        
    def twice(self):
        self.v = twofold(slef.v)
        self.__display()
        
c = CCM(12)

c.var = 20
print(c.__dict__)
print(c.__module__)
# print(c.__name__)
print(c.__doc__)
print(c.__base__)