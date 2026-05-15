class Solution(object):

    def numRescueBoats(self, people, limit):

        people.sort()

        left = 0
        right = len(people) - 1

        boat = 0

        while left <= right:

            # Nếu chở được cả 2
            if people[left] + people[right] <= limit:

                left += 1

            right -= 1

            boat += 1

        return boat