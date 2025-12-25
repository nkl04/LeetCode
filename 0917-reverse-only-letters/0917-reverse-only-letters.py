class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def is_letter(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

        l,r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if not is_letter(s[l]):
                l += 1
            elif not is_letter(s[r]):
                r -= 1
            elif is_letter(s[l]) and is_letter(s[r]):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


        