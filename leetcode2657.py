class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        
        cur = 0
        s_a, s_b = set(), set()
        for i in range(len(A)):
            if A[i] == B[i]:
                cur += 1
            else:
                if A[i] in s_b:
                    s_b.discard(A[i])
                    cur += 1
                else:
                    s_a.add(A[i])
                
                if B[i] in s_a:
                    s_a.discard(B[i])
                    cur += 1
                else:
                    s_b.add(B[i])

            res[i] = cur
        
        return res
