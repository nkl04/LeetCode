class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        F = defaultdict(lambda: 0)
        for i in range(k - 1):
            F[nums[i]] += 1
        
        for i in range(len(nums) - k + 1):
            F[nums[i + k -1]] += 1
            xx = x
            for n in range(-50,51):
                xx -= F[n]
                if xx <= 0:
                    res.append(n)
                    break
            if res[-1] >= 0:
                res[-1] = 0
            F[nums[i]] -= 1
        return res

            

                