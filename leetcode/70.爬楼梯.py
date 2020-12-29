#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# 整数
#1 1 
#2 1+1 or 2
#3 1+1+1 or 2+1 or 1+2



# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2 : return n
        a,b,c=1,2,0
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return c
# @lc code=end

