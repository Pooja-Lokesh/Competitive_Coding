# Trapping rain water problem.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        min_,max_= 0,len(height)-1
        areas = 0
        while min_ != max_:
            if height[min_] < height[max_]:
                areas = max((max_-min_)*height[min_],areas)
                min_ +=1
            else:
                areas = max((max_-min_)*height[max_],areas)
                max_ -=1
        return areas