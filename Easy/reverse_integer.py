class Solution:
    def reverse(self, x: int) -> int:
        
        # setting a flag for negative or not negtaive 
        flag = 0
        
        if flag == 0:
            if x < 0:
                flag = -1
            else:
                flag = 1
        
        num = abs(x)
        
        s = str(num)
        l = list(s)
        
        # reversing the list 
        
        i = 0
        j = len(l) - 1
        
        while i < j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i+=1
            j-=1
        
        #converting the list to string and then to an integer
        l2 = "".join(l)
        final = int(l2)
        
        # Multiply with the flag to get the final answer with the original           sign (negative or positive)
        reversed_num = final*flag
        
        if reversed_num <= -2**31 or reversed_num >= 2**31:
            return 0 
        
        return reversed_num