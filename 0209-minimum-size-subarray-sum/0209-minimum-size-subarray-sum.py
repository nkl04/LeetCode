class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        s = 0
        left = 0
        for right in range(len(nums)):
            s += nums[right]
            
            while s >= target:
                minLen = min(minLen, right - left + 1)
                s -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen
            
                
            

        