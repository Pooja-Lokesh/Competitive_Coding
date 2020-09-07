
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string1 =""
        for i in s:
            if i.isalnum():
                string1 +=i.lower()
            else:
                continue
        return string1 == string1[::-1]