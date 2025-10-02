class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeats, seens = set(), set()

        for l in range(len(s) - 9):
            sub = s[l:l+10]
            if sub in seens:
                repeats.add(sub)
            seens.add(sub)
            l += 1

        return list(repeats)