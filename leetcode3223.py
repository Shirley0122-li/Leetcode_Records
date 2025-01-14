class Solution:
    def minimumLength(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        res = 0
        for char in count:
            # delete 2 once having 3
            if count[char] % 2 == 0:
                res += 2
            else:
                res += 1

        return res