class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left, right = 0, 10
        repeats = set()
        seens = set()
        for i in range(len(s) - 9):
            sub = s[left:right]
            if sub in seens:
                repeats.add(sub)
            else:
                seens.add(sub)
            right += 1
            left += 1

        return list(repeats)