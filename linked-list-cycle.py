class Solution(object):

    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # Nếu gặp nhau
            if slow == fast:

                return True

        return False