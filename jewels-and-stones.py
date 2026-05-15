class Solution:
    def numJewelsInStones(self, jewels, stones):
        
        count = 0

        # duyệt từng ký tự trong stones
        for stone in stones:

            # nếu stone nằm trong jewels
            if stone in jewels:
                count += 1

        return count