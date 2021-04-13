# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 500] 内 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 109 
#  
#  Related Topics 链表 双指针 
#  👍 538 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # 求链表长度
        cur = head
        n = 0
        # 移动cur到链表末端，求得长度n
        while cur:
            cur = cur.next
            n += 1
        # 求k%n的值
        j = k % n
        # k%n==0 即k==0 或 k为n的倍数，那么仍然为原来的链表
        if j == 0:
            return head
        # 快慢指针
        slow = fast = head
        # 先让fast移动j个位置
        while j:
            fast = fast.next
            j -= 1
        # 再同时移动slow和fast，让slow处于倒数第k+1个位置
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 重整链表
        newhead = slow.next
        slow.next = None  # 断开
        fast.next = head
        return newhead
# leetcode submit region end(Prohibit modification and deletion)
