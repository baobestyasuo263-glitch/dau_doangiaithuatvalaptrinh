class Solution(object):
    def topKFrequent(self, nums, k):

        dem = {}

        # Đếm số lần xuất hiện
        for i in nums:
            if i in dem:
                dem[i] += 1
            else:
                dem[i] = 1

        # Sắp xếp theo số lần xuất hiện giảm dần
        sapxep = sorted(dem.items(), key=lambda x: x[1], reverse=True)

        ketqua = []

        # Lấy k phần tử đầu
        for i in range(k):
            ketqua.append(sapxep[i][0])

        return ketqua