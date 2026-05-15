class Solution(object):

    def countWords(self, words1, words2):

        dem1 = {}
        dem2 = {}

        # Đếm words1
        for w in words1:

            if w in dem1:
                dem1[w] += 1
            else:
                dem1[w] = 1

        # Đếm words2
        for w in words2:

            if w in dem2:
                dem2[w] += 1
            else:
                dem2[w] = 1

        ketqua = 0

        # Kiểm tra xuất hiện đúng 1 lần ở cả 2
        for w in dem1:

            if dem1[w] == 1 and w in dem2 and dem2[w] == 1:

                ketqua += 1

        return ketqua