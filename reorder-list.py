class Solution(object):

    def reorderList(self, head):

        if not head:
            return

        # Tìm middle
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # Reverse nửa sau
        prev = None
        curr = slow

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge
        first = head
        second = prev

        while second.next:

            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2