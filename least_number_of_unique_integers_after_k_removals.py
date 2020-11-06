class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        l_count = []
        
        s = set(arr)
        
        for i in s:
            l_count.append(arr.count(i))
            
        l_count = sorted(l_count)
            
        sum_check = 0
        
        for i in range(len(l_count)):
            sum_check += l_count[i]
            if sum_check > k:
                return len(l_count[i:])
            if sum_check == k:
                return len(l_count[i:]) - 1