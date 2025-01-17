class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        original = [0] * len(derived)
        for i in range(len(derived) - 1):
            original[i+1] = original[i]^derived[i]
        
        return original[-1]^derived[-1] == original[0]