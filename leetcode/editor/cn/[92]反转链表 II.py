# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 849 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 哨兵节点
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        count = 1  # 计步器
        # 移动pre到left前一个节点
        while pre and count < left:
            pre = pre.next
            count += 1
        cur = pre.next  # cur指向pre.next
        tail = cur  # tail=cur , 也是反转后部分的最后一个节点
        while cur and count <= right:
            nxt = cur.next  # nxt 指向当前cur的下一个节点
            cur.next = pre.next  # 当前cur.next指向pre.next
            pre.next = cur  # 当前pre.next指向cur
            tail.next = nxt  # tail.next指向nxt
            cur = nxt  # 令cur=nxt
            count += 1
        # 返回dummy.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
