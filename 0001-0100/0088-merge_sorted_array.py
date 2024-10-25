from typing import List


class Solution:

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Don't return anything! modify nums1 in-place instead.
        """
        k = m + n - 1
        if k != len(nums1) + len(nums2):
            return

        m -= 1
        n -= 1

        while k >= 0:
            if m < 0:
                nums1[k] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[k] = nums1[m]
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1
