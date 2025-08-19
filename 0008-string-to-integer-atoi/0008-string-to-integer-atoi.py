class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        sign = 1
        if i < len(s) and (s[i] == "+" or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit

            if num > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN

            i += 1

        return sign * num