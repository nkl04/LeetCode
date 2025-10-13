class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        for i in range(0,x//2+1):
            if i ** 2 == x or (i**2 < x and (i+1)**2 > x):
                return i
                
        