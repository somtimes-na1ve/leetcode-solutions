from typing import List


class Solution:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        n = len(nums)
        k = 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
