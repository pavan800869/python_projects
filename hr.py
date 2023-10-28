class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        n = x
        r = 0
        s = 0
        while x!=0:
            r = x%10
            s = s*10 + r
            x=x//10

        if s == n:
            print("true")
        else:
            print("false")


if __name__=="__main__":
    x = int(input())
    ob = Solution()
    ob.isPalindrome(x)


        