class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
            
class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
      def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
            
if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(9)
    print Solution().reverseList(head)
