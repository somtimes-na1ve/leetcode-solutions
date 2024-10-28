from typing import List


class Solution:

    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        # using hash table
        mapping = {}

        for i, num in enumerate(nums):
            if i > k:
                mapping.pop(nums[i - k - 1])
            if num in mapping:
                return True
            mapping[num] = i

        return False
