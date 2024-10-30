from typing import List


class Solution:

    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        if k == n:
            return

        def reverse(arr: List[int], l: int, r: int) -> None:
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
