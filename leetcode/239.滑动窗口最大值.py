#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import  deque
        queue=deque()
        res=[]
        def mover(i):
            while queue and queue[0]<=i-k : 
                queue.popleft()
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)

        for i in range(k):
            mover(i)
        res.append(nums[queue[0]])

        for i in range(k,len(nums)):
            mover(i)
            res.append(nums[queue[0]])
        
        return res     
# @lc code=end

