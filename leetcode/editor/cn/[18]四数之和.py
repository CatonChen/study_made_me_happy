# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        if not nums or n < 4:
            return res

        for p in range(n - 3):
            if p > 0 and nums[p] == nums[p - 1]:
                continue
            if nums[p] + nums[p + 1] + nums[p + 2] + nums[p + 3] > target:
                break
            if nums[p] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            # k = p + 1
            for k in range(p + 1, n - 2):
                if k > p + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[p] + nums[k] + nums[k + 1] + nums[k + 2] > target:
                    break
                if nums[p] + nums[k] + nums[n - 1] + nums[n - 2] < target:
                    continue
                i, j = k + 1, n - 1
                while i < j:
                    s = nums[p] + nums[k] + nums[i] + nums[j]
                    if s == target:
                        res.append([nums[p], nums[k], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i + 1]:  # 条件与三数之和不同
                            i += 1
                        i += 1
                        while i < j and nums[j] == nums[j - 1]:  # 条件与三数之和不同
                            j -= 1
                        j -= 1
                    elif s > target:
                        j -= 1
                    else:
                        i += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
