from typing import List


class Solution:

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        n = len(strs)
        m = min([len(s) for s in strs])

        for j in range(m):
            ch = strs[0][j]
            cnt = 1
            for i in range(1, n):
                if strs[i][j] == ch:
                    cnt += 1
            if cnt != n:
                return strs[0][0:j]

        return strs[0][0:m]
