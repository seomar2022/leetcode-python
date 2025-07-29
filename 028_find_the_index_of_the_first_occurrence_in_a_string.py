class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i+needle_len] == needle:  
                return i    
        return -1
    
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string?envType=problem-list-v2&envId=nz1q6a0h
#July 29, 2025