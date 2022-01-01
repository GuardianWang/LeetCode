"""
LC 257
Given the root of a binary tree, return all root-to-leaf paths in any order.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root):
  res = []
  cur = []
  find_all_paths(root, res, cur)
  return res


def find_all_paths(root, paths, cur_path):
  if not root:
    return
  cur_path.append(str(root.val))
  if root.left is None and root.right is None:
    paths.append("->".join(cur_path))
  find_all_paths(root.left, paths, cur_path)
  find_all_paths(root.right, paths, cur_path)
  cur_path.pop()


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths " +
        ": " + str(find_paths(root)))


main()


"""
Time O(NlogN)
Space O(NlogN)
"""

