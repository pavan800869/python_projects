#Given ranges and display the grades of the students.
import sys
global l1 

l1 =[]
def display():
    for i in l1:
        print(i)
def main():
    print(''' 
    This is a stack you can enter and delete elements for the stack by giving the operations.
          1. Push, enter the element to push into the stack.
          2. Pop. the last element will be popped from the stack.
          3. Display, shows the elements in the stack.
          4. Exit from the stack.
    ''')
    while True:
        choice = int(input("1.Push\n2.Pop\n3.Display\n4.Exit\n"))
        if choice == 1:
            n = int(input("Enter the element: "))
            l1.append(n)
            continue

        elif choice == 2:
            l1.pop()
            continue

        elif choice == 3:
            display()
            continue

        else:
            sys.exit


if __name__=="__main__":
    main()
            

