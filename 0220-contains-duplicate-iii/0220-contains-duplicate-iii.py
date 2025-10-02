from sortedcontainers import SortedSet
from bisect import bisect_left
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedSet()

        left = 0
        for num in nums: # right pointer
            pos = window.bisect_left(num - valueDiff)

            if pos < len(window) and window[pos] <= num + valueDiff:
                return True
            window.add(num)
            if len(window) > indexDiff:
                window.remove(nums[left])
                left += 1
        return False

    