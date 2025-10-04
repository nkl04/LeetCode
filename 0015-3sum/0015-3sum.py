class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = sorted(nums)

        for i in range(0,len(l)-1):
            if i > 0 and l[i-1] == l[i]:
                continue
            j,k = i+1,len(l)-1
            while k > j:
                s = l[i] + l[j] + l[k]
                if s == 0:
                    res.append([l[i],l[j],l[k]])
                    j += 1
                    k -= 1
                    while j < k and l[j] == l[j-1]:
                        j += 1
                    while j < k and l[k] == l[k+1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                elif s < 0:
                    j +=1
        return res