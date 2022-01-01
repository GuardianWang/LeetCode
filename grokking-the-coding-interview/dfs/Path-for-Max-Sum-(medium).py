"""
Given a binary tree, find the root-to-leaf path with the maximum sum.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root):
  res = []
  cur_path = []
  find_max(root, res, cur_path, 0)
  return res


max_sum = 0
def find_max(root, res, cur_path, cur_sum):
  global max_sum
  if not root:
    return 
  cur_sum += root.val
  cur_path.append(root.val)
  if (not root.left) and (not root.right):
    if cur_sum > max_sum:
      max_sum = cur_sum
      res.clear()
      res.extend(cur_path)

  find_max(root.left, res, cur_path, cur_sum)
  find_max(root.right, res, cur_path, cur_sum)
  cur_path.pop()


def main():

  root = TreeNode(12)
  root.left = TreeNode(8)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths max sum " + str(find_paths(root)))


main()


"""
Time O(N)
Space O(N)
"""

