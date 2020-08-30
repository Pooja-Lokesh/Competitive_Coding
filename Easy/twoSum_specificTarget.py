# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = []
        
        for i in range(len(numbers)):
            j = i + 1
            while j < len(numbers) :
                if numbers[i] + numbers[j] == target:
                    index.append(i + 1)
                    index.append(j + 1)
                    return index
                j+=1