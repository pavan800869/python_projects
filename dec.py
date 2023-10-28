### Decorator ###
# nested function 
def outer():
    number = 5
    
    def inner():
        print(number)
         
    inner()
# first class citizen
def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x+y
def sub(x, y):
    return x - y


# Outer functions are objects, whereas inner are attributes just like class and object. 


#executions

# print(apply(add,5,3))
# print(apply(sub,10,6))


#closure

# def close():
#     x = 5
#     def inner():
#         print(x)
#     return inner

# closure = close()
# closure()

def add_to_five(num):
    def inner():
        print(num +5)
    return inner

fifteen = add_to_five(10)
fifteen()

