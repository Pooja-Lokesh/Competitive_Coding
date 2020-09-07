class Solution:
    def titleToNumber(self, s: str) -> int:
        
        l = len(s)
        sum = 0

        for i in range(l-1,-1,-1):
            n = (26**i)*(ord(s[-(i-l+1)])-64)
            sum += n
            
        return sum