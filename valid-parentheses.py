class Solution(object):

    def isValid(self, s):

        stack = []

        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for c in s:

            # Ngoặc mở
            if c in "([{":

                stack.append(c)

            else:

                # Sai nếu stack rỗng
                if not stack:
                    return False

                # Sai cặp ngoặc
                if stack.pop() != pairs[c]:
                    return False

        return len(stack) == 0
        