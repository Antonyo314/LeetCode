# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        print(l1)

        n1 = ''

        while True:
            try:
                n1 += str(l1.val)
                l1 = l1.next
            except:
                break

        n1 = int(n1[::-1])

        n2 = ''

        while True:
            try:
                n2 += str(l2.val)
                l2 = l2.next
            except:
                break

        n2 = int(n2[::-1])

        n = str(n1 + n2)

        l = None
        for i in n:
            l = ListNode(int(i), l)

        return l