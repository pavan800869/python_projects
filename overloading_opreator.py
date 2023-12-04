class Comp:
    def __init__(self):
        self.r = 0
        self.i = 0
    def set (self, r, i):
        self.r = r
        self.i = i

    def display(self):
        print(self.r, "+", self.i,"i")

    def __add__(self, c):
        t = Comp()
        t.r = self.r + c.r 
        t.i = self.i + c.i 
        return t 

c1 = Comp()
c1.set(2,6)
c1.display()
c2 = Comp()
c2.set(3,8)
c2.display()
c3 = Comp()
c3 = c1+c2
c3.display()

#Program 2
# class Pastry:
#     def __init__(self, f1, price):
#         self.f1 = f1
#         self.price = price 
#     def showDetails(self):
#         print(f"Flavour: {self.f1}")
#         print(f"Price: {self.price}")
# #This function gives the less than comparison of given objects 
#     def __lt__(self, p):
#         if self.price < p.price:
#             return True
#         else:
#             return False 
        
# p = Pastry("Butterscotch", 100)
# p1 = Pastry("Pineapple", 20)



# if p < p1:
#     p.showDetails()
# else:
#     p1.showDetails()
        