# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 *
#  。 
# 
#  示例 1: 
# 
#  输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2 
# 
#  示例 2: 
# 
#  输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10 
#  Related Topics 分治算法 
#  👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 终止条件：如果输入是数字，返回数字
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, exp in enumerate(expression):
            if exp in ['+', '-', '*']:  # 运算符
                # 递归自身求运算符左右解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # print('left: ', left, ' right:', right)
                # 遍历左右子解
                for l in left:
                    for r in right:
                        # 根据运算符合并解
                        if exp == '+':
                            res.append(l + r)
                        elif exp == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res

# leetcode submit region end(Prohibit modification and deletion)
