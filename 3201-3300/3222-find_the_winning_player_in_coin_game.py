class Solution:

    @staticmethod
    def losing_player(x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) else "Bob"
