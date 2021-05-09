# 给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
#  
# 
#  示例 2: 
# 
#  
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"] 
# 
#  示例 3: 
# 
#  
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"] 
# 
#  示例 4: 
# 
#  
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
#  
# 
#  示例 5: 
# 
#  
# 输入: num = "3456237490", target = 9191
# 输出: [] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num.length <= 10 
#  num 仅含数字 
#  
#  Related Topics 分治算法 
#  👍 212 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # 回溯
        def backtrace(num, target, exp, tmp, ans, res):
            # 当num用完，且ans==目标值是，表示找到正确的表达式
            if len(num) == 0 and ans == target:
                res.append(exp)
                return
            else:
                for i in range(1, len(num) + 1):
                    # 跳过0开头的非一位数
                    if i > 1 and num[0] == '0':
                        continue
                    a = int(num[0:i])  # 选取的数字
                    # print('exp:', exp, '   a:', a)
                    if exp == '':
                        # 初始
                        backtrace(num[i:], target, num[0:i], a, a, res)
                    else:
                        # 加法
                        backtrace(num[i:], target, exp + '+' + num[0:i], a, ans + a, res)
                        # 减法
                        backtrace(num[i:], target, exp + '-' + num[0:i], -a, ans - a, res)
                        # 乘法
                        backtrace(num[i:], target, exp + '*' + num[0:i], tmp * a, ans - tmp + tmp * a, res)

        res = []
        backtrace(num, target, '', 0, 0, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
