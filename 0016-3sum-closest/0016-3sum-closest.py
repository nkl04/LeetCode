class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minGap = float('inf')
        n = len(nums)
        nums.sort()
        res = 0
        
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < minGap:
                    minGap = abs(s - target)
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: 
                    return res
        return res