class Solution:
    def specialArray(self, nums: List[int]) -> int: 
        
        m = max(nums)
        d = {}
        
        for i in range(m+1):
            c = [x for x in nums if x >= i]
            d[i] = len(c)
            
        for k,v in d.items():
            if k == v:
                return k
            
        return -1
            
        