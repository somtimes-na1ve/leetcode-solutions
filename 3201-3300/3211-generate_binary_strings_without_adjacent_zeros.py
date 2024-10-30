from typing import List


class Solution:

    @staticmethod
    def valid_strings(n: int) -> List[int]:
        ans = []
        path = [''] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append("".join(path))
                return

            # setup '1'
            path[i] = '1'
            dfs(i + 1)

            # setup '0'
            if i == 0 or path[i - 1] == '1':
                path[i] = '0'
                dfs(i + 1)

        dfs(0)
        return ans
