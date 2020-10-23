class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, v in enumerate(s):
            if v not in dic:
                dic[v] = i
            elif v in dic:
                dic[v] = "rep"
        
        for d in dic:
            if dic[d] != "rep":
                return dic[d]
        return -1



'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
            
            
        for c in s:
            if d[c] == 1:
                return s.index(c)
        
        return -1
''' 