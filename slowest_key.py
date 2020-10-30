class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        l = []
        ls = list(keysPressed)
        l2 = []
        l.append(releaseTimes[0])
        
        f = 0
        i = 1
        while i < len(releaseTimes):
            l.append(releaseTimes[i] - releaseTimes[f])
            f += 1
            i += 1 
        
        m = max(l)
        count = l.count(m)
        
        if count == 1:
            return ls[l.index(m)]
        
        for i in range(len(l) - 1):
            if l[i] == m:
                l2.append(ls[i])
        
        return max(l2)
            