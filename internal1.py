#WAPP to Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triangle from polygon and write methods to get the details of their dimension and hence calculate the area.

class Polygon:
    def set(self):
        raise NotImplementedError
    def area(self):
        raise NotImplementedError

class Rectangle(Polygon):
    def set(self):
        self.l = int(input("Enter length:\n")) 
        self.b = int(input("Enter Breadth:\n"))
    def area(self):
        return self.l*self.b
    
class Triangle(Polygon):
    def set(self):
        self.h = int(input("Enter height:\n")) 
        self.b = int(input("Enter base:\n"))
    def area(self):
        return 0.5*self.h*self.b
    
r = Rectangle()
t = Triangle()
t.set()
r.set()
print(f"The area of rectangle is {r.area()}")
print(f"The area of triangle is {t.area()}")
