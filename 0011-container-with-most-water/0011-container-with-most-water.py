class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        v_max = 0
        while right > left:
            v = (right - left) * min(height[right], height[left])
            if v > v_max:
                v_max = v
            if height[right] > height[left]:
                    left += 1
            else: 
                    right -= 1
        return v_max   
            

        