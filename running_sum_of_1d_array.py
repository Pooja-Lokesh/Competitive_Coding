class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        l = []
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            l.append(sums)
            
        return l