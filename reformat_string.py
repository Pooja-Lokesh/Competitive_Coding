class Solution:
    def reformat(self, s: str) -> str:
        
        c = []
        n = []
        l = []
        
        if len(s) == 1:
            return s
        
        for i in range(len(s)):
            if s[i].isnumeric() == True:
                n.append(s[i])
            else:
                c.append(s[i])
                
        if len(c) == 0 or len(n) == 0:
            return ""
        
        if abs(len(c) - len(n)) > 1:
            return ""
        
        l1 = len(n)
        l2 = len(c)
        
        
        if l1 > l2:
            for i in range(len(s)):
                if i % 2 == 0:
                    l.append(n.pop(0))
                else:
                    l.append(c.pop(0))
                    
                    
        elif l1 == l2:
            for i in range(len(s)):
                if i % 2 == 0:
                    l.append(n.pop(0))
                else:
                    l.append(c.pop(0))
                    
        else :
            for i in range(len(s)):
                if i % 2 == 0:
                    l.append(c.pop(0))
                else:
                    l.append(n.pop(0))
                    
        return "".join(l)
        