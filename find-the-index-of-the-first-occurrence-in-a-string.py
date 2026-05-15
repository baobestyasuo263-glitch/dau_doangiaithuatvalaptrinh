class Solution(object):

    def strStr(self, haystack, needle):

        # Độ dài chuỗi cần tìm
        m = len(needle)

        # Duyệt từng vị trí có thể bắt đầu
        for i in range(len(haystack) - m + 1):

            # Cắt chuỗi từ i đến i+m
            if haystack[i:i + m] == needle:

                return i

        # Không tìm thấy
        return -1