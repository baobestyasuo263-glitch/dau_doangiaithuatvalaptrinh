class Solution(object):

    def dailyTemperatures(self, temperatures):

        n = len(temperatures)

        ketqua = [0] * n

        stack = []

        for i in range(n):

            # Khi gặp nhiệt độ cao hơn
            while stack and temperatures[i] > temperatures[stack[-1]]:

                idx = stack.pop()

                ketqua[idx] = i - idx

            stack.append(i)

        return ketqua