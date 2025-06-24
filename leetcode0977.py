class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0 for _ in range(len(nums))]
        index = len(nums) - 1
        nums = [x**2 for x in nums]

        while l < r:
            if nums[l] <= nums[r]:
                res[index] = nums[r]
                r -= 1
            else:
                res[index] = nums[l]
                l += 1
            index -= 1
        
        res[0] = nums[l]
        return res