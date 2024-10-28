class Solution:

    @staticmethod
    def word_pattern(pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        selected = set()
        mapping = {}
        for word, c in zip(words, pattern):
            if word not in mapping:
                if c in selected:
                    return False
                selected.add(c)
                mapping[word] = c
                continue
            if c != mapping[word]:
                return False

        return True
