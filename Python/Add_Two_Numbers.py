# https://goo.gl/c7HTf3 code for code below visualizer.
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
   def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
