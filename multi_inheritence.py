class Parent:
    def fun(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child class")
class GrandChild(Child):
    def fun3(self):
        print("This is Grandchild class")

obj = GrandChild()
obj.fun()
obj.fun2()
obj.fun3()


print("Program ends")