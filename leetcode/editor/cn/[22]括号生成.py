# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 回溯算法 
#  👍 1758 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 深度优先搜索
        def dfs(cur_str, left, right):
            # 终止条件
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < n:
                dfs(cur_str + '(', left + 1, right)
            if right < left:
                dfs(cur_str + ')', left, right + 1)

        res = []
        dfs('', 0, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
