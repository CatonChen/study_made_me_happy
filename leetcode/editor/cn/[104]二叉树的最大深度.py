# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 递归 
#  👍 783 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        queue = []  # 建立队列
        queue.append(root)
        while queue:
            size = len(queue)
            while size > 0:
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size -= 1  # 处理好一个节点
            ans += 1  # 处理好一层
        return ans

# leetcode submit region end(Prohibit modification and deletion)
