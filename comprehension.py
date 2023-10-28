# nums = range(1, 101)
#  This is a comprehensive way of writing a python code. This is so useful and easy to write.
# halves = [num for num in nums if num%3 == 0] 
# print(halves)

# x = {number: letter for number, letter in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
# print(x)
fizzbuzz = {
    "fizz" : [n for n in range(1, 101) if n%3 == 0],

    "buzz" : [n for n in range(1, 101) if n%7 == 0]

}

fizzbuzz = {key : set(value) for key, value in fizzbuzz.items()}

fizzbuzz['fizzbuzzes'] = {n for n in fizzbuzz['fizz'].intersection(fizzbuzz['buzz'])}

print(fizzbuzz)