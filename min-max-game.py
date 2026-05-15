class Solution(object):

    def minMaxGame(self, nums):

        # Lặp tới khi còn 1 số
        while len(nums) > 1:

            moi = []

            # Duyệt từng cặp
            for i in range(len(nums)//2):

                # Index chẵn
                if i % 2 == 0:

                    moi.append(
                        min(nums[2*i], nums[2*i+1])
                    )

                # Index lẻ
                else:

                    moi.append(
                        max(nums[2*i], nums[2*i+1])
                    )

            nums = moi

        return nums[0]