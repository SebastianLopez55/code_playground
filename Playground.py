# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node is None:
                return

            path.append(str(node.val))

            if not node.left and not node.right:  # if reach a leaf
                paths.append("->".join(path))  # add path to result
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()  # backtrack to explore other paths

        dfs(root, [])
        return paths

        # O(n) time.
        # O(n) space.

    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # if reach a leaf
                    paths.append(path)  # add path to result
                else:
                    path += "->"  # extend the current path
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return paths
