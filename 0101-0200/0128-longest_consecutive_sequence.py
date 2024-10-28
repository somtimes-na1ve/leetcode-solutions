from typing import List


class Solution:

    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        s = set(nums)

        for num in nums:
            if num not in s:
                continue

            s.remove(num)
            possible = [num - 1, num + 1]
            cur = 1

            while possible[0] or possible[1]:
                if possible[0] is not None and possible[0] in s:
                    cur += 1
                    s.remove(possible[0])
                    possible[0] -= 1
                else:
                    possible[0] = None

                if possible[1] is not None and possible[1] in s:
                    cur += 1
                    s.remove(possible[1])
                    possible[1] += 1
                else:
                    possible[1] = None

            ans = max(ans, cur)

        return ans
