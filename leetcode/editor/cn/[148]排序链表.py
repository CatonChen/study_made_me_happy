# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内 
#  -105 <= Node.val <= 105 
#  
#  Related Topics 排序 链表 
#  👍 1081 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 快慢指针找中间节点
    def find_mid(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 合并两个有序链表
    def merge_two_list(self, left, right):
        dummy = ListNode()
        dummyhead = dummy
        while left and right:
            if left.val < right.val:
                dummyhead.next = left
                left = left.next
            else:
                dummyhead.next = right
                right = right.next
            dummyhead = dummyhead.next
        dummyhead.next = left if left is not None else right
        return dummy.next

    # 归并排序
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left_end = self.find_mid(head)
        right_start = left_end.next
        left_end.next = None
        left, right = self.sortList(head), self.sortList(right_start)
        return self.merge_two_list(left, right)

# leetcode submit region end(Prohibit modification and deletion)
