# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SE
# E"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CB"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？ 
#  Related Topics 数组 回溯算法 
#  👍 890 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()  # 记录坐标是否被使用

        # 递归
        def backtrace(i, j, k):
            if board[i][j] != word[k]:
                return False  # 矩阵字母与单词字母不匹配
            else:
                if k == len(word) - 1:
                    return True  # 字母全部匹配
            visited.add((i, j))  # 记录已使用的坐标
            # 四联通方向搜索
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                # 1、矩阵范围内 2、坐标未被重复使用 3、递归结果为真
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and backtrace(ni, nj, k + 1):
                    return True
            # 回溯，恢复坐标使用状态
            visited.remove((i, j))
            return False  # 找不到

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrace(i, j, 0):
                        return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
