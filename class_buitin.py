class List_item:
    def __init__(self,l):
        self.l = l

    def __getitem__(self, i):
        return self.l[i]
    
    def __setitem__(self, i, v):
        self.l[i] = v

l1 = List_item([10,12,13,14,16,1,2,44,40])

print(l1[5])
l1[1] = 11

print(l1.l)

print("Check att: ",hasattr(l1, 'l'))
print("get attr: ", getattr(l1, 'l'))
setattr(l1, 'l', [37,47,27])

print("get attr: ", getattr(l1, 'l'))

if hasattr(l1, 'l'):
    delattr(l1, 'l')

try:
    print("Get attr: ", getattr(l1, 'l'))
except Exception as e:
    isinstance(e, AttributeError)
    print("There is not attribute available.")


        