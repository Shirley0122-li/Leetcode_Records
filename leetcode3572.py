class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        if len(set(x)) < 3:
            return -1
        
        loc_x = defaultdict(list)
        for i, v in enumerate(x):
            loc_x[v].append(i)
        
        res, count = 0, 0
        while count < 3:
            i = y.index(max(y))
            res += y[i]
            for index in loc_x[x[i]]:
                y[index] = 0
            count += 1
        
        return res