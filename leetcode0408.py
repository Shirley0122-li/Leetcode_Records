class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        num = 0
        for char in abbr:
            if char.isdigit():
                if num == 0 and int(char) == 0:
                    return False

                num = num*10 + int(char)
            
            if char.isalpha():
                if num != 0:
                    i += num
                    num = 0
                if i >= len(word) or word[i] != char:
                    return False
                i += 1
        
        return i + num == len(word)