class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for ch in s:
            if ch not in {"*", "#", "%"}:
                res.append(ch)
            elif ch == "#":
                res.extend(res)
            elif ch == "%":
                res.reverse()
            else:  # ch == "*"
                if res:
                    res.pop()
        return ''.join(res)