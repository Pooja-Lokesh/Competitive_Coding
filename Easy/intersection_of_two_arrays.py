class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        count = []
        
        for i in nums1:
            for i in nums2:
                if i not in d.keys():
                    c = min(nums2.count(i), nums1.count(i))
                    d[i] = c

        for i in d.keys():
            for j in range(d[i]):
                count.append(i)
                
        return count