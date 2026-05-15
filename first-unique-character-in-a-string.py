class Solution(object):

    def firstUniqChar(self, s):

        # Dictionary để đếm ký tự
        dem = {}

        # Đếm số lần xuất hiện
        for c in s:

            if c in dem:
                dem[c] += 1
            else:
                dem[c] = 1

        # Duyệt lại chuỗi để tìm ký tự unique đầu tiên
        for i in range(len(s)):

            # Nếu ký tự xuất hiện đúng 1 lần
            if dem[s[i]] == 1:

                return i

        # Không có ký tự unique
        return -1