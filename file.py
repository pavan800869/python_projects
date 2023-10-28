def remember(thing):
    #to open a file
    f = open("data.txt", 'a')
    #to write in some info
    f.write(thing + '\n')
    #to close a file
    f.close()

if __name__=='__main__':
    remember(input("What to remember: "))

# with open("filename", "opening mode") as file_ptr:
#     all the functions that are to be included
# This is the efficient method.
# This method closes the file by itself.