class Solution:

    @staticmethod
    def get_smallest_string(s: str) -> str:
        n = len(s)
        digits = list(s)

        for i in range(1, n):
            x, y = digits[i - 1], digits[i]
            if x > y and ord(x) % 2 == ord(y) % 2:
                digits[i - 1], digits[i] = y, x
                break

        return ''.join(digits)
