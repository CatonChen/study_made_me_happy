# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -109 <= matix[i][j] <= 109 
#  每行的所有元素从左到右升序排列 
#  每列的所有元素从上到下升序排列 
#  -109 <= target <= 109 
#  
#  Related Topics 二分查找 分治算法 
#  👍 627 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 二分查找
    def binarysearch(self, line, target):
        left, right = 0, len(line)
        while left <= right:
            mid = left + (right - left) // 2
            # print(line[mid])
            if line[mid] == target:
                return True
            elif line[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        # 遍历矩阵
        for line in matrix:
            if line[0] == target or line[-1] == target:
                return True
            elif line[0] > target or line[-1] < target:
                continue
            elif line[0] < target < line[-1]:
                if self.binarysearch(line, target):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
