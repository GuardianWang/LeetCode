"""
LC 543
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path . The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# 遍历访问的思想
class TreeDiameter:
  def find_diameter(self, root):
    # 1. either max(left_d, right_d), or
    # 2. left_height + right_height + 1
    return self.find_d(root)[0]

  def find_d(self, root):
    if not root:
      return 0, 0  # diameter, depth
    l_dia, l_nodes = self.find_d(root.left)
    r_dia, r_nodes = self.find_d(root.right)
    nodes = max(l_nodes, r_nodes) + 1
    return max(l_dia, r_dia, l_nodes + r_nodes + 1), nodes   


def main():
  # 5, 7
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()


"""
Time O(N)
Space O(N)
"""

