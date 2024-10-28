from typing import List


class Solutions:

    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        l, n = 0, len(nums)
        ans = []

        while l < n:
            r = l + 1
            while r < n and nums[r] == nums[r - 1] + 1:
                r += 1
            if r - l == 1:
                ans.append(f"{nums[l]}")
            else:
                ans.append(f"{nums[l]}->{nums[min(r - 1, n - 1)]}")
            l = r

        return ans
