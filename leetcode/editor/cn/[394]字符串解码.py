# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
#  Related Topics 栈 深度优先搜索 
#  👍 706 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s) - 1
        # 逆序遍历s
        while i >= 0:
            if s[i].isdigit() is False:
                stack.append(s[i])
                i -= 1
                # print(stack)
            else:
                num = ''
                while i >= 0 and s[i].isdigit() is True:
                    num = s[i]+num  # 这里不用+=，保持数字顺序
                    i -= 1
                # print(num[::-1])
                sub = ''
                while stack[-1] != ']':
                    tmp = stack.pop()
                    if tmp != '[':
                        sub += tmp
                # print(sub)
                stack.pop()  # 弹出 ]
                # print(stack)
                # print(sub)
                sub = int(num) * sub  # 解码
                # print(sub)
                stack.append(sub)  # 解码后再入栈
                # print(stack)
        # print(stack)
        stack.reverse()
        return ''.join(stack)
    # leetcode submit region end(Prohibit modification and deletion)
