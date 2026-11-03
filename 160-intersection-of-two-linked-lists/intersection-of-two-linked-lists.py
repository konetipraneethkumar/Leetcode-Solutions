# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ First approach """
    #def length(self,head:ListNode):
    #   current = head
    #   count = 0
    #   while current:

    #       count +=1
    #       current = current.next
    #   return count


    #def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

    #   s1 = self.length(headA)
    #   s2 = self.length(headB)
    #   extra =0
    #   current1 = headA
    #   current2 = headB
    #   if s1>s2:
    #       extra = s1-s2
    #   else:
    #       extra = s2-s1

    #   for i in range(extra):
    #       if s1 >s2:
    #           current1 = current1.next
    #       else:
    #           current2 = current2.next
    #   while current1 and current2:
    #       if current1 == current2:
    #           return current1
    #       current1 = current1.next
    #       current2 = current2.next
    #   return None
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        current1 = headA
        current2 = headB
        while current1 or current2:
            if current1 is current2:
                return current1
            if current1 is None:
                current1 = headB
            else:
                current1 = current1.next
            if current2 is None:
                current2 = headA
            else:
                current2 = current2.next
            
        return None


        