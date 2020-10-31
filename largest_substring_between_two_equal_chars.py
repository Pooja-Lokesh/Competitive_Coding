class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        final = []
        
        i = 0
        j = 0
        
        while i < len(s):
            j = i + 1
            while j < len(s):
                if s[i] == s[j]:
                    final.append(len(s[i+1:j]))
                j += 1
            i += 1
                
        if len(final) != 0:
            return max(final)
        
        return -1
        