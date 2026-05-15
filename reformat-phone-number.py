class Solution(object):

    def reformatNumber(self, number):

        s = ""

        # Lấy chỉ chữ số
        for c in number:

            if c.isdigit():
                s += c

        ketqua = []

        i = 0

        while len(s) - i > 4:

            ketqua.append(s[i:i+3])
            i += 3

        # Nếu còn 4 số -> chia 2-2
        if len(s) - i == 4:

            ketqua.append(s[i:i+2])
            ketqua.append(s[i+2:i+4])

        else:
            ketqua.append(s[i:])

        return "-".join(ketqua)