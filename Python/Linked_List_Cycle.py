#code visualized https://goo.gl/orWmPe
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                return True
        return False

##
# with cycle 
##
if __name__ == "__main__":
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().hasCycle(head)
    
##
# without cycle
##
if __name__ == "__main__":
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    print Solution().hasCycle(head)
