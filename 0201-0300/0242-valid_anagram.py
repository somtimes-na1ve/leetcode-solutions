from collections import Counter


class Solution:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)
        for c in t:
            counter[c] -= 1

        return all(y == 0 for _, y in counter.items())
