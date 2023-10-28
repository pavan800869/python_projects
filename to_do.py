
todo_list = [ ]


def add_to_list(new_item):
    todo_list.append(new_item)
    print("Added {}. list now has {} items".format(new_item, len(todo_list)))

def update():
    n = int(input("Enter the place number:\n"))
    new_item = input(', ')
    todo_list[n] = new_item
    return new_item


def show_help():
    print("Enter items you need to pick up at the store")
    print("""
Enter Done to stop
Enter Help to help
Enter Show to shw the list""")
def show_list():
    i = 0
    print("Here is your list")
    for item in todo_list:
        print(i, item)
        i += 1
while True:
    new_item = input(", ")
    
    if new_item == 'Done':
        break
    elif new_item == 'Update':
        update()
        continue
    elif new_item == 'Help':
        show_help()
        continue
    elif new_item == 'Show':
        show_list()
        continue
    add_to_list(new_item)
    #Show command
    




