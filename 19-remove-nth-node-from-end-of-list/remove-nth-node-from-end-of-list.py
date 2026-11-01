# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    # Brute Force Approach
    def lengthOfLinks(self, head: ListNode | None):
        # Finding LinkedList Length 
        current = head
        count = 0
        while current:
            count +=1
            current = current.next
        return count

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # length of the linkedlist
        dammi =ListNode(0)
        dammi.next = head
        current = dammi
        length = self.lengthOfLinks(head)
        nodePos = length - n
        
        for i in range(nodePos):
            current = current.next
        current.next = current.next.next
        return dammi.next
        
    """
# Using Two Pointers
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dammi = ListNode(0, head)
        slow = fast = dammi
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dammi.next

        