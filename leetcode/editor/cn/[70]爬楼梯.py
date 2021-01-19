# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        #  当n==1或2时，返回n
        if n == 1 or n == 2:
            return n
        # 初始化变量
        a, b, tmp = 1, 2, 0
        for i in range(3, n + 1):
            # print(i)
            tmp = a + b
            a = b
            b = tmp
        # 返回结果
        return tmp
# leetcode submit region end(Prohibit modification and deletion)


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     @functools.lru_cache(100)
#     def climbStairs(self, n: int) -> int:
#         #递归
#         if n==1 or n==2:
#             return n
#         return self.climbStairs(n-1)+self.climbStairs(n-2)
# leetcode submit region end(Prohibit modification and deletion)
