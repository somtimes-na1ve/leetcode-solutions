from typing import List


class Solution:

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in mapping:
                return [i, mapping[val]]
            mapping[num] = i

        return [-1, -1]
