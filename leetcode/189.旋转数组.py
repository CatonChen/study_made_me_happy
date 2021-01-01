#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def swap(i,j):
            while (i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        swap(0,n-k-1)
        swap(n-k,n-1)
        swap(0,n-1)

# @lc code=end

