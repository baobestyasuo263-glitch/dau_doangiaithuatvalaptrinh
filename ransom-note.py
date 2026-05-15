class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        dem = {}

        # đếm ký tự trong magazine
        for c in magazine:

            if c in dem:
                dem[c] += 1
            else:
                dem[c] = 1

        # kiểm tra ransomNote
        for c in ransomNote:

            if c not in dem or dem[c] == 0:
                return False

            dem[c] -= 1

        return True
        