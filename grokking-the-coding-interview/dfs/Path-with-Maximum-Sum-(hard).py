"""
LC 124
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class MaximumPathSum:

  def find_maximum_path_sum(self, root):
    # either
    # 1. max(left_sum, right_sum), or
    # 2. left_single_sum + right_single_sum + root.val
    return self.find_max(root)[0]

  def find_max(self, root):
    if not root:
      # in case meet negative values
      return -float('inf'), 0
    l_max_sum, l_single_sum = self.find_max(root.left)
    r_max_sum, r_single_sum = self.find_max(root.right)
    # similar to local sequence matching
    # need max(, 0) to allow starting from the current node 
    # when other branches are negative values
    return max(l_max_sum, r_max_sum, max(l_single_sum, 0) + max(r_single_sum, 0) + root.val), \
      max(l_single_sum, r_single_sum, 0) + root.val


def main():
  # 6, 31, -1, 4
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(2)
  root.left.left = TreeNode(-4)
  root.right = TreeNode(3)
  root.right.right = TreeNode(-5)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()


"""
Time O(N)
Space O(N)
"""

