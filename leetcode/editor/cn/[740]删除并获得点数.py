# 给你一个整数数组 nums ，你可以对它进行一些操作。 
# 
#  每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] +
#  1 的元素。 
# 
#  开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  1 <= nums[i] <= 104 
#  
#  Related Topics 动态规划 
#  👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        from collections import Counter
        hashmap = Counter(nums)
        # print(hashmap)
        # 动态规划
        maxlen = max(hashmap.keys())
        # 初始化
        # dp = [0] * (maxlen + 1)
        # dp[1] = 1 * hashmap[1]
        # for i in range(2, maxlen + 1):
        #     # 状态转移
        #     dp[i] = max(dp[i - 1], dp[i - 2] + i * hashmap[i])
        # return dp[-1]
        # 状态压缩
        first, second = 0, 1 * hashmap[1]
        for i in range(2, maxlen + 1):
            first, second = second, max(first + i * hashmap[i], second)
        return second
# leetcode submit region end(Prohibit modification and deletion)
