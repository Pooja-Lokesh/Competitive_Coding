"""
# Using set : This takes around 5000ms more than not using set
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        u = set(nums)
        for num in u:
            if nums.count(num) == 1:
                return num
"""

# This is faster
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()