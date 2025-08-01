class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                temp = [1 for _ in range(i+1)]
                for j in range(1, i):
                    temp[j] = res[-1][j-1] + res[-1][j]
                res.append(temp)
        
        return res
                