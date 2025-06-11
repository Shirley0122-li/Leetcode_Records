class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [i, dic[n]]
            else:
                dic[target - n] = i