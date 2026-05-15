class Solution(object):

    def canAliceWin(self, n):

        # Số đá cần lấy đầu tiên
        stone = 10

        # True = Alice
        # False = Bob
        alice = True

        # Tiếp tục khi còn lượt
        while stone > 0:

            # Nếu không đủ đá để lấy
            if n < stone:

                # Người hiện tại thua
                return not alice

            # Lấy đá
            n -= stone

            # Giảm số đá lượt sau
            stone -= 1

            # Đổi người chơi
            alice = not alice

        # Nếu hết lượt mà chưa thua
        return False