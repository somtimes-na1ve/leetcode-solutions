from typing import Optional

from common.treenode import TreeNode


class Solution:

    @staticmethod
    def max_depth(root: Optional[TreeNode]) -> int:
        return 0 if root is None \
                 else 1 + max(Solution.max_depth(root.left), Solution.max_depth(root.right))
