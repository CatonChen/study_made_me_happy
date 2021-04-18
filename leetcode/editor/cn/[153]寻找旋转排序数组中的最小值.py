# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。 
# 
#  请找出其中最小的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -5000 <= nums[i] <= 5000 
#  nums 中的所有整数都是 唯一 的 
#  nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转 
#  
#  Related Topics 数组 二分查找 
#  👍 341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 生序数组
            if nums[left] < nums[right]:
                return nums[left]
            # 0-mid是生序 min值在mid-right之间
            elif nums[mid] > nums[right]:
                left = mid + 1
            # mid=0是生序数组的第一个元素，或 在生序数组中mid-1的元素>mid的元素
            elif mid == 0 or nums[mid - 1] > nums[mid]:
                return nums[mid]
            else:  # mid-right是生序，min在left-mid之间
                right = mid - 1
# leetcode submit region end(Prohibit modification and deletion)
