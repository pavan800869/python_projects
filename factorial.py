#To write a recursive factorial program
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
    
if __name__=="__main__":
    n = int(input("Enter a number: "))
    result = fact(n)
    print(result)