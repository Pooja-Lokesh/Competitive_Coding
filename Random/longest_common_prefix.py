class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) 

# one more way is to initialize the prefix string as the first elelemt in the strings array, 
# loop through all the other eleemst in the array of string, remove the characters which arent on the 
# subsequent strings.
         