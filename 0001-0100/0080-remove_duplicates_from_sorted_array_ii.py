from typing import List


class Solution:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        def solve(k: int) -> int:
            u = 0
            for num in nums:
                if u < k or num != nums[u - k]:
                    nums[u] = num
                    u += 1
            return u

        return solve(2)
