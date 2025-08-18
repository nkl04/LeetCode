class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        _dict = {}
        for i in range(numRows):
            _dict[i] = ""
        i = 0
        check = True
        for item in s:
            _dict[i] += item
            if i == numRows - 1:
                check = False
            elif i == 0:
                check = True
            
            if check:
                i += 1
            else: 
                i -= 1
        res = ""
        for i in _dict:
            res += _dict[i]
        
        return res

            
            
        