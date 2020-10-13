class Solution:
    def addDigits(self, num: int) -> int:

        def singleDigit(n):
            l = list(str(n))
            sum_digit = 0
            
            for i in l:
                sum_digit += int(i)
                
            return sum_digit
        
        sum_d = num
        
        while len(list(str(sum_d))) > 1:
            sum_d = singleDigit(sum_d)
            
        return sum_d
            
        