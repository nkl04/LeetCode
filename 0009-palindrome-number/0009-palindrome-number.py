class Solution:
    def isPalindrome(self, x: int) -> bool:
        i,j = 0,0
        str_x = str(x)
        str_y = str_x[::-1]
        if str_x == str_y:
            return True
        else:
            return False



        