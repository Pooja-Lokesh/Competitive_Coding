# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """s.reverse() 
        print(s)"""
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
            
        print(s)        