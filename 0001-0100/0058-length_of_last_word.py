class Solution:

    @staticmethod
    def length_of_last_word(s: str) -> int:
        # s.rstrip()
        # return len(s) - s.rfind(' ') - 1

        r = len(s) - 1
        while r >= 0 and s[r] == ' ':
            r -= 1

        l = r
        while l >= 0 and s[l] != ' ':
            l -= 1

        return r - l
