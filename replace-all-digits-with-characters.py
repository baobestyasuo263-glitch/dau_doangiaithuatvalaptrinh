class Solution(object):

    def replaceDigits(self, s):

        ketqua = ""

        for i in range(len(s)):

            # Nếu là chữ
            if i % 2 == 0:

                ketqua += s[i]

            else:
                # Dịch ký tự
                moi = chr(ord(s[i-1]) + int(s[i]))

                ketqua += moi

        return ketqua