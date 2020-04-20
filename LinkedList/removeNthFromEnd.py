# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        pre = ListNode(0)
        pre.next = head
        while head:
            length += 1
            head = head.next

        if length == 1:
            return []

        dummy = ListNode(0)
        cur = dummy
        cur.next = pre.next
        track = pre.next
        i = 0
        while track:
            cur = cur.next
            if i == length - n - 1:
                track.next = track.next.next
            track = track.next
            cur.next = track
            i += 1
        return dummy.next

    def printList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

a = ListNode(1)

s = Solution()
print(s.printList(a))
ap = s.removeNthFromEnd(a, 2)
print(s.printList(ap))