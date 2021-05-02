# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  数独的解法需 遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  
# 
#  
#  
#  
#  示例： 
# 
#  
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5","."
# ,".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".","."
# ,"3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"
# ],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],["
# .",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"
# ],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["
# 4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","
# 6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","
# 5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
# 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字或者 '.' 
#  题目数据 保证 输入数独仅有一个解 
#  
#  
#  
#  
#  Related Topics 哈希表 回溯算法 
#  👍 827 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 设置row\col\block
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        # 遍历矩阵，将已有的数字进行处理
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + (j // 3)].remove(val)
                else:
                    empty.append((i, j))

        # print(row)
        # print(col)
        # print(block)
        # print(empty)

        # 回溯
        def backtrace(n):
            # 当n==len(empty)时，表示已经处理完了，返回True
            if n == len(empty):
                return True
            i, j = empty[n]
            b = (i // 3) * 3 + (j // 3)
            for val in row[i] & col[j] & block[b]:  # 集合的交集运算 &是位于运算符
                # print('n:', n, ' : ', row[i] & col[j] & block[b], '  val:', val)
                board[i][j] = str(val)  # 将i,j坐标更新为val
                # 移除已占用的数字
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                # 递归
                if backtrace(n + 1):
                    return True
                # 恢复状态
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False

        backtrace(0)
# leetcode submit region end(Prohibit modification and deletion)
