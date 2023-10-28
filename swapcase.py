def swap_case(s):
    ans = s.split(' ')
    ans1 = (i.upper() for i in ans) #comprehensive code line    
    return ans1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)