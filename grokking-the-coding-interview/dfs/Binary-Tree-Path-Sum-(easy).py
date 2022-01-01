"""
LC 112
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, s):
    # a node with no right child is not a leaf
    if root is None:
        return False
    if root.left is None and root.right is None:
        return s == root.val
    return has_path(root.left, s - root.val) or has_path(root.right, s - root.val)


def main():
  # T, F
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()


"""
Time O(N)
Space O(N): a linked list
"""

