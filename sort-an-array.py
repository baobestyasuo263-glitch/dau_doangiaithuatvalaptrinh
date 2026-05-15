class Solution(object):

    def sortArray(self, nums):

        # Nếu mảng có 0 hoặc 1 phần tử thì đã sắp xếp sẵn
        if len(nums) <= 1:
            return nums

        # Tìm vị trí giữa mảng
        mid = len(nums) // 2

        # Chia mảng thành 2 nửa
        trai = nums[:mid]
        phai = nums[mid:]

        # Đệ quy tiếp tục chia nhỏ
        trai = self.sortArray(trai)
        phai = self.sortArray(phai)

        # Gọi hàm gộp 2 mảng đã sắp xếp
        return self.merge(trai, phai)


    def merge(self, trai, phai):

        ketqua = []

        i = 0   # chạy trong mảng trái
        j = 0   # chạy trong mảng phải

        # So sánh từng phần tử của 2 mảng
        while i < len(trai) and j < len(phai):

            # Nếu phần tử bên trái nhỏ hơn
            if trai[i] < phai[j]:

                ketqua.append(trai[i])
                i += 1

            else:

                ketqua.append(phai[j])
                j += 1

        # Thêm các phần tử còn dư của mảng trái
        while i < len(trai):

            ketqua.append(trai[i])
            i += 1

        # Thêm các phần tử còn dư của mảng phải
        while j < len(phai):

            ketqua.append(phai[j])
            j += 1

        return ketqua