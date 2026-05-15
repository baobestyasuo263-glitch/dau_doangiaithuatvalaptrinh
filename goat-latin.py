class Solution(object):

    def toGoatLatin(self, sentence):

        words = sentence.split()

        nguyen_am = "aeiouAEIOU"

        ketqua = []

        # Duyệt từng từ
        for i in range(len(words)):

            word = words[i]

            # Nếu bắt đầu bằng nguyên âm
            if word[0] in nguyen_am:

                moi = word + "ma"

            else:
                # Chuyển chữ đầu xuống cuối
                moi = word[1:] + word[0] + "ma"

            # Thêm a theo vị trí
            moi += "a" * (i + 1)

            ketqua.append(moi)

        return " ".join(ketqua)