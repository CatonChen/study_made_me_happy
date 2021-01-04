#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[none_zero],nums[i]=nums[i],nums[none_zero]
                none_zero+=1
                
# @lc code=end

