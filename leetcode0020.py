class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if stack:
                    prev = stack.pop()
                else:
                    return False
                if char == ')':
                    if prev != '(':
                        return False
                elif char == ']':
                    if prev != '[':
                        return False
                elif char == '}':
                    if prev != '{':
                        return False
        
        if stack:
            return False
        else:
            return True