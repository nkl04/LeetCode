class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)   
        for i in range(n-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                k,l = j+1,n-1
                while l > k:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        res.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                        while l > k and nums[l+1] == nums[l]:
                            l -= 1
                        while l > k and nums[k-1] == nums[k]:
                            k += 1
                    elif s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                
        return [list(t) for t in res]
        