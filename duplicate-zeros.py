class Solution(object):

    def duplicateZeros(self, arr):

        i = 0

        while i < len(arr) - 1:

            # Nếu gặp số 0
            if arr[i] == 0:

                # Chèn thêm 0
                arr.insert(i, 0)

                # Xóa phần tử cuối
                arr.pop()

                # Bỏ qua số 0 mới chèn
                i += 1

            i += 1