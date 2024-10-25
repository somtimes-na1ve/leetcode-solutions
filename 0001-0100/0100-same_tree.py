from typing import Optional

from common.treenode import TreeNode


class Solution:

    @staticmethod
    def is_same_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 is None or t2 is None:
            return t1 is t2
        return t1.val == t2.val \
            and Solution.is_same_tree(t1.left, t2.left) \
            and Solution.is_same_tree(t1.right, t2.right)
