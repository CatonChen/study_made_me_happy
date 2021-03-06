# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。 
# 
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 
# 0（代表水）包围着。 
# 
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。) 
# 
#  
# 
#  示例 1: 
# 
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# 
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。 
# 
#  示例 2: 
# 
#  [[0,0,0,0,0,0,0,0]] 
# 
#  对于上面这个给定的矩阵, 返回 0。 
# 
#  
# 
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。 
#  Related Topics 深度优先搜索 数组 
#  👍 482 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # dfs
    def dfs(self, grid, x, y):
        # 终止条件
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        ans = 1
        # 探索相邻的1
        ans += self.dfs(grid, x + 1, y)
        ans += self.dfs(grid, x - 1, y)
        ans += self.dfs(grid, x, y + 1)
        ans += self.dfs(grid, x, y - 1)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = set()
        # 遍历矩阵
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans.add(self.dfs(grid, i, j))
                else:
                    ans.add(0)
        return max(ans)
# leetcode submit region end(Prohibit modification and deletion)
