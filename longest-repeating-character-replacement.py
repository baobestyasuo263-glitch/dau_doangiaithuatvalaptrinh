class Solution(object):

    def characterReplacement(self, s, k):

        count = {}

        left = 0

        maxf = 0
        max_len = 0

        for right in range(len(s)):

            c = s[right]

            # Đếm ký tự
            count[c] = count.get(c, 0) + 1

            # Số lần xuất hiện lớn nhất
            maxf = max(maxf, count[c])

            # Nếu cần đổi quá k ký tự
            while (right - left + 1) - maxf > k:

                count[s[left]] -= 1

                left += 1

            # Cập nhật kết quả
            max_len = max(max_len, right - left + 1)

        return max_len