from typing import List


class Solution:

    @staticmethod
    def majority_elements(nums: List[int]) -> int:
        # Moore Vote
        ans, cnt = nums[0], 0

        for num in nums:
            if cnt == 0:
                ans = num
            cnt += 1 if ans == nums else -1

        return ans
