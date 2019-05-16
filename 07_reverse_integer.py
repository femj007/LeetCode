#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.23%)
# Total Accepted:    645.5K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        if (x < -2**31) or (x > 2**31-1):
            return 0
        
        neg = 1
        if (x < 0):
            neg = -1
            x = -x
        ans = 0
        st = str(x)
        l = len(st)
        i = l - 1
        while (x > 0):
            t = x % 10
            ans = ans + t * 10**i
            i = i - 1
            x = int(x / 10)
        if (ans < -2**31) or (ans > 2**31-1):
            return 0
        return ans*neg
