class Solution:

    @staticmethod
    def is_isomorphic(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        selected = set()
        mapping = {}
        for x, y in zip(s, t):
            if x not in mapping:
                if y in selected:
                    return False
                selected.add(y) # record another str if selected
                mapping[x] = y
                continue
            if mapping[x] != y:
                return False

        return True
