from typing import Optional
from common.treenode import TreeNode


class Solution:

    @staticmethod
    def count_nodes(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def height(node: Optional[root]) -> int:
            return 0 if node is None else 1 + max(height(root.left), height(root.right))

        lt_height = height(root.left)
        rt_height = height(root.right)

        if lt_height == rt_height:
            return Solution.count_nodes(root.right) + (1 << lt_height)
        else:
            return Solution.count_nodes(root.left) + (1 << rt_height)
