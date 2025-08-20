class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        a = x
        while a > 0:
            y = y * 10 + a % 10
            a //= 10
        if x == y:
            return True
        else:
            return False
        
        



        