"""
https://leetcode.com/problems/reverse-string/
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

#測試程式        
if __name__ == '__main__':
    s = Solution()
    print(s.reverseString('hello!'))
