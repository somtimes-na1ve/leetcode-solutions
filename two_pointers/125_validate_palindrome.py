class Solution:

    @staticmethod
    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l <= r:
            # 跳过不相关的字符
            while l <= r and not s[l].isalnum(): l += 1
            while l <= r and not s[r].isalnum(): r -= 1

            if l <= r and s[l] != s[r]:
                return False

        return True