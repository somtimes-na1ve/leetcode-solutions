from typing import List


class Solution:

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k