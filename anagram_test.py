class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        
        if len(s) != 0 or len(t) != 0:
            for n in ls:
                if n not in lt:
                    return False
                return True
         
        else:
            return False

        # return dict(Counter(s))==dict(Counter(t))
        # Counter is a sub-class which is used to count hashable objects. 
        # It implicitly creates a hash table of an iterable when invoked.
        # .element() can be sued to access all the elements in the iterable