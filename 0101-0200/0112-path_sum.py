from typing import Optional
from common.treenode import TreeNode


class Solution:

    @staticmethod
    def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        target -= root.val
        return target == 0 if root.left is None and root.right is None \
                else (Solution.has_path_sum(root.left, target) or Solution.has_path_sum(root.right, target))
