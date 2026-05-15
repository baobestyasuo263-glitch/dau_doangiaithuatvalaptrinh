class Solution(object):

    def isPalindrome(self, s):

        moi = ""

        # Chỉ lấy chữ và số
        for c in s:

            if c.isalnum():

                moi += c.lower()

        # So sánh với chuỗi đảo ngược
        return moi == moi[::-1]