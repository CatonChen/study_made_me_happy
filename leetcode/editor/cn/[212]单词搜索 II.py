# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l"
# ,"v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 12 
#  board[i][j] 是一个小写英文字母 
#  1 <= words.length <= 3 * 104 
#  1 <= words[i].length <= 10 
#  words[i] 由小写英文字母组成 
#  words 中的所有字符串互不相同 
#  
#  Related Topics 字典树 回溯算法 
#  👍 355 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 创建字典树
        WORD_KEY = '$'
        trie = {}
        for word in words:  # 单词
            node = trie
            for letter in word:  # 字母
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word  # 单词用$标记出来

        rownum = len(board)
        colnum = len(board[0])
        matchedWords = []

        # 递归回溯
        def backtracking(row, col, parent):
            letter = board[row][col]
            currnode = parent[letter]
            word_match = currnode.pop(WORD_KEY, False)
            # print(word_match)
            if word_match:
                matchedWords.append(word_match)

            # 将字母标记为#，即已使用
            board[row][col] = '#'
            # 探索当前单元格四周单元格 上右下左
            for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_x, new_y = row + x, col + y
                if new_x < 0 or new_y < 0 or new_x >= rownum or new_y >= colnum:
                    continue
                if not board[new_x][new_y] in currnode:
                    continue
                backtracking(new_x, new_y, currnode)
            # 回溯，恢复状态
            board[row][col] = letter
            # 剪枝：当前currnode已经遍历过了，从父节点中删除
            if not currnode:
                parent.pop(letter)

        # 遍历board的所有单元格
        for row in range(rownum):
            for col in range(colnum):
                if board[row][col] in trie:
                    # print(board[row][col])
                    backtracking(row, col, trie)

        return matchedWords
# leetcode submit region end(Prohibit modification and deletion)
