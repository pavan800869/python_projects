# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print('@', end=' ')
#     print('\n')
# for i in range(5):
#     for j in range(5):
#         print('*', end=' ')
#     print('\n')
for i in range(1,5):
    print(*range(1, i+2))

for i in range(4):
    print("*"*4)

for i in range(1,5):
    print(*[i]*i)