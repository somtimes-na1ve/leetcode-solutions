from typing import List


class Solution:

    @staticmethod
    def results_array(nums: List[int], k: int) -> List[int]:
        ans = [-1] * (len(nums) - k + 1)
        cnt = 1

        for i, num in enumerate(nums):
            cnt = cnt + 1 if num == nums[i - 1] + 1 else 1
            if cnt >= k:
                ans[i - k + 1] = num

        return ans
