class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = height.copy()
        right = height.copy()
        
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        
        print(left)

        right[-1] = height[-1]
        res = 0
        for i in range(len(height)-1)[::-1]:
            right[i] = max(right[i+1], height[i])
            res += min(left[i], right[i]) - height[i]
        
        return res