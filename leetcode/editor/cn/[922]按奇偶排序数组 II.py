# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。 
# 
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。 
# 
#  你可以返回任何满足上述条件的数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  Related Topics 排序 数组 
#  👍 201 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 先按奇偶归类
        odd = []
        even = []
        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        # 再根据下标修改愿数组结果
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums
# leetcode submit region end(Prohibit modification and deletion)
