from operator import invert
from typing import Optional
from common.treenode import TreeNode


class Solution:

    @staticmethod
    def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root

        lt = Solution.invert_tree(root.left)
        rt = Solution.invert_tree(root.right)

        root.left = rt
        root.right = lt

        return root
