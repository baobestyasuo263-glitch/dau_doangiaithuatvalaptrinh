class Solution(object):

    def isPalindrome(self, x):

        # Số âm không phải palindrome
        if x < 0:

            return False

        # So sánh với số đảo
        return str(x) == str(x)[::-1]