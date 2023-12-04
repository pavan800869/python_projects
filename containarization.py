class First:
    def set(self, v):
        self.v = v
    def get(self):
        return self.v
    
class Second:
    def __init__(self, v):
        self.f = First()
        self.f.set(v)

    def display(self):
        print(self.f.get())


s = Second(10)
s.display()
