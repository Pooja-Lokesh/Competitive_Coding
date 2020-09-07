class Solution:
    def isHappy(self, n: int) -> bool:
        if len(str(n)) == 1:
            if(n==1 or n == 7): return True
            else: return False
        numbers_array = [int(i) for i in str(n)]
        total_count = 0
        for i in numbers_array:
            total_count += i**2
        return self.isHappy(total_count)