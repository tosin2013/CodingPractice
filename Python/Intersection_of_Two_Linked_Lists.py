###
##  See code visualized https://goo.gl/j7JgdF
###
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
     def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        begin, tailA, tailB = None, None, None
        
        # a->c->b->c
        # b->c->a->c
        while curA and curB:
            if curA == curB:
                begin = curA
                break
                
            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break
            
            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break
        
        return begin
###
# Without intersection
###           
if __name__ == '__main__':
    headA = ListNode(1)
    headA.next = ListNode(3)
    headA.next.next = ListNode(6)
    headA.next.next.next = ListNode(444)
    headA.next.next.next.next = ListNode(9)
    headB = ListNode(1)
    headB.next = ListNode(3)
    headB.next.next = ListNode(6)
    headB.next.next.next = ListNode(444)
    headB.next.next.next.next = ListNode(9)
    print Solution().getIntersectionNode(headA, headB)

###
## With intersection 
###
if __name__ == '__main__':
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(9)
    headA.next.next.next.next = ListNode(10)
    intersection = headA.next.next.next.next
    headB = ListNode(0)
    headB.next = ListNode(3)
    headB.next.next = ListNode(8)
    headB.next.next.next = ListNode(9)
    headB.next.next.next.next = intersection
    print Solution().getIntersectionNode(headA, headB)
