class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def find_diff_all_equal(a):
            l = []
            
            f = 0
            i = 1
            while i < len(a):
                l.append(a[i]-a[f])
                i += 1
                f += 1
                
            return l
        
        final = []
        
        m = len(l)
        
        for i in range(m):
            a = nums[l[i]:r[i]+1]
            c = find_diff_all_equal(sorted(a))
            if c.count(c[0]) == len(c):
                final.append(True)
            else:
                final.append(False)
        
        return final
        