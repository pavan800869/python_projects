class Parent:
    def fun(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child classs")

obj = Child()
obj.fun()
obj.fun2()

print("Program ends")