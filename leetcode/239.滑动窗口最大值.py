#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # queue = collections.deque()

        # for i in range(len(nums)):
        #     while queue and nums[queue[-1]] < nums[i]:
        #         queue.pop()
        #     queue.append(i)

        #     if queue[0] <= i-k:
        #         queue.popleft()
        #     if i >= k-1:
        #         res.append(nums[queue[0]])
        # return res

        win = []
        ret = []
        for i ,v in enumerate(nums):
            if i>=k and win[0] <=i-k: win.pop(0)

            while win and nums[win[-1]]<=v: win.pop()
            win.append(i)
            
            if i>=k-1: ret.append(nums[win[0]])
        return ret 
            
# @lc code=end

