class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        v_max = 0
        while left < right:
            v = (right - left) * min(height[right],height[left])
            if v > v_max:
                v_max = v
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return v_max
        