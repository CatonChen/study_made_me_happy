# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X"
# ,"X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 526 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        root = x
        self.add(root)
        while self.father[root] is not None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            o_father = self.father[x]
            self.father[x] = root
            x = o_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        m, n = len(board), len(board[0])

        # 定义node
        def node(x, y):
            return x * n + y

        uf = UnionFind()
        dummy = node(m, n)
        uf.add(dummy)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':  # 对O操作
                    # 边界坐标
                    if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                        uf.merge(node(x, y), dummy)
                    else:  # 非边界但相邻
                        for mx, my in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if 0 <= mx < m and 0 <= my < n and board[mx][my] == 'O':
                                uf.merge(node(x, y), node(mx, my))
        # 更新board
        for x in range(m):
            for y in range(n):
                if uf.is_connected(node(x, y), dummy):
                    board[x][y] = 'O'
                else:
                    board[x][y] = 'X'
# leetcode submit region end(Prohibit modification and deletion)
