#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1=ListNode(0)   #小链表
        dummy2=ListNode(0)   #大链表
        p=dummy1
        q=dummy2
        while head:
            if head.val<x:
                p.next=head
                p=p.next
            else:
                q.next=head
                q=q.next
            head=head.next
        q.next=None
        p.next=dummy2.next
        return dummy1.next

# @lc code=end

