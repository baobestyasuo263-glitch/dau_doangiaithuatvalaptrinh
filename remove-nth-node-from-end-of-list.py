class Solution(object):

    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Fast đi trước n bước
        for i in range(n):

            fast = fast.next

        while fast.next:

            fast = fast.next
            slow = slow.next

        # Xóa node
        slow.next = slow.next.next

        return dummy.next