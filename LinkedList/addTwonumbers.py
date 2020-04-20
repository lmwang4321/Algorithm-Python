class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwonumbers(self, l1, l2):
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 or l2:
            if l1 is None:
                x = 0
            else:
                x = l1.val

            if l2 is None:
                y = 0
            else:
                y = l2.val

            sum = x + y + carry

            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            cur.next = ListNode(carry)

        return pre.next




s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

res = s.addTwonumbers(l1, l2)