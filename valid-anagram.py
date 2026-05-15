class Solution:
    def isAnagram(self, s, t):

        # Nếu độ dài khác nhau
        if len(s) != len(t):
            return False

        # Sắp xếp và so sánh
        return sorted(s) == sorted(t)