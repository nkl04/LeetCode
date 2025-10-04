
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = list()
        dq = deque(maxlen=k)
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            if (r + 1) >= k:
                maxs.append(nums[dq[0]])
                l += 1
        
        return maxs
            


        