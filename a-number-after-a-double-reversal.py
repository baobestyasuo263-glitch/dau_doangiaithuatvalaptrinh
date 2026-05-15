class Solution(object):

    def isSameAfterReversals(self, num):

        # Nếu số tận cùng là 0
        # sẽ mất số 0 khi đảo
        return num == 0 or num % 10 != 0