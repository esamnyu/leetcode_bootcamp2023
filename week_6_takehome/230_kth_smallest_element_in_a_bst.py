from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an array to hold the elements in in-order traversal
        elements = []

        # Helper function to perform in-order traversal
        def inorder(node):
            if not node:
                return

            # Traverse the left subtree
            inorder(node.left)
            # Append the current node's value
            elements.append(node.val)
            # Traverse the right subtree
            inorder(node.right)

        # Perform in-order traversal starting from the root
        inorder(root)

        # Return the kth smallest element
        # Subtract 1 from k because list indices start at 0
        return elements[k - 1]

# Example usage
# Constructing a simple tree for demonstration
#       3
#      / \
#     1   4
#      \
#       2
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

solution = Solution()
k = 2
print(solution.kthSmallest(root, k))  # Should print the 2nd smallest element in the BST
