"""
https://leetcode.com/problems/single-number/

Given an array of integers, every element appears twice except for one. Find that single one.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        #解法 : 運用xor (1^(2^2)^(3^3)^(5^5)) => 1^0^0^0 => 1
        for num in nums:
            result ^= num
        return result

#測試程式
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,2,3,3,5,5]))
