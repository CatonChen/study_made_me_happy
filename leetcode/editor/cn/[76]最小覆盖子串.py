# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 1064 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        # 初始化need
        for c in t:
            need[c] += 1
        needcnt = len(t)  # 初始化needcnt
        i = 0
        res = (0, len(s) + 1)  # res[1]也可为float('inf')
        # 枚举s
        for j, c in enumerate(s):
            if need[c] > 0:
                needcnt -= 1
            need[c] -= 1
            if needcnt == 0:  # 窗口元素符合条件
                while True:
                    c = s[i]
                    if need[c] == 0:  # 必须包含的元素
                        # print(need)
                        break
                    need[c] += 1  # 排除不必要的元素
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)  # 保存窗口的最小长度
                    # print(res)
                need[s[i]] += 1  # i增加一个位置，寻找新窗口
                needcnt += 1
                i += 1
        return '' if len(s) < res[1] else s[res[0]:res[1] + 1]  # res[1]没有被更新过，即表示没有符合的子串。
# leetcode submit region end(Prohibit modification and deletion)
