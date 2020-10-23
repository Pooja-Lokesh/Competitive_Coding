class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

# Solution 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

# Solution 3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sublist = [[]] 
        max_sum = []
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
      
        for i in range(len(nums) + 1): 
            for j in range(i + 1, len(nums) + 1): 
                sub = nums[i:j] 
                sublist.append(sub)
                
        sublist.remove([])
                
        for l in range(len(sublist)):
            max_sum.append(sum(sublist[l]))