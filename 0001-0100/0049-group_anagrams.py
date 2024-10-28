from collections import defaultdict
from typing import List


class Solution:

    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            mapping[''.join(sorted(s))].append(s)
        return list(mapping.values())
