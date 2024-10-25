from typing import Optional
from common.treenode import TreeNode


class Solution:

    @staticmethod
    def is_symmetric_tree(root: Optional[TreeNode]) -> bool:

        def helper(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None or t2 is None:
                return t1 is t2
            return t1.val == t2.val \
                and helper(t1.left, t2.right) \
                and helper(t2.left, t1.right)

        return helper(root, root)