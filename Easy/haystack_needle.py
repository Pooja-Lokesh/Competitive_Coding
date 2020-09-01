class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==" " or needle==" ":
            return 0
        else:
            return haystack.find(needle)
        