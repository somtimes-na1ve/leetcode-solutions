from collections import Counter


class Solution:

    @staticmethod
    def can_construct(ransom_note: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for ch in ransom_note:
            counter[ch] -= 1
            if counter[ch] < 0:
                return False

        return True
