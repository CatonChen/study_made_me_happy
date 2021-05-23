# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。 
# 
#  已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。 
# 
#  每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎
# ，则可以在之后的操作中 重复使用 这枚鸡蛋。 
# 
#  请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？ 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
# 如果它没碎，那么肯定能得出 f = 2 。 
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
#  
# 
#  示例 2： 
# 
#  
# 输入：k = 2, n = 6
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：k = 3, n = 14
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 100 
#  1 <= n <= 104 
#  
#  Related Topics 数学 二分查找 动态规划 
#  👍 625 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 创建字典消除重复子问题
        memo = {}

        # 递归
        def dp(K, N):
            # 递归终止条件
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 二分查找
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                # 左右边界
                t1 = dp(K - 1, mid - 1)  # 鸡蛋碎
                t2 = dp(K, N - mid)  # 鸡蛋没碎
                if t1 > t2:
                    hi = mid - 1
                    res = min(res, t1 + 1)
                else:
                    lo = mid + 1
                    res = min(res, t2 + 1)
            memo[(K, N)] = res  # 记忆已经找到的解
            return res

        return dp(k, n)
# leetcode submit region end(Prohibit modification and deletion)
