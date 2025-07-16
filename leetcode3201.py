class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res_0, res_1, res_0_no_init = 1, 1, 0
        for n in nums[1:]:
            if n%2 == nums[0]%2:
                res_0 += 1
                if res_1%2 == 0:
                    res_1 += 1
            
            else:
                res_0_no_init += 1
                if res_1%2 == 1:
                    res_1 += 1
        
        return max(res_0, res_1, res_0_no_init)