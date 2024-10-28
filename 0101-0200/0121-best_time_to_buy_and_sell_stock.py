from typing import List


class Solution:

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        ans = 0
        mi_ = prices[0]

        for price in prices:
            ans = max(ans, price - mi_)
            mi_ = min(mi_, price)

        return ans
