class Solution(object):

    def countHillValley(self, nums):

        arr = [nums[0]]

        # Xóa phần tử trùng liên tiếp
        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:

                arr.append(nums[i])

        dem = 0

        for i in range(1, len(arr) - 1):

            # Hill
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                dem += 1

            # Valley
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:

                dem += 1

        return dem