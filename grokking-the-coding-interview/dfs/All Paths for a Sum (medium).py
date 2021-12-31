"""
LC 113
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  res = []
  cur_path = []
  find_all_paths(root, required_sum, res, cur_path)
  return res

def find_all_paths(root, required_sum, path_list, cur_path):
  if root is None:
    return
  cur_path.append(root.val)
  if root.left is None and root.right is None:
    if required_sum == root.val:
      path_list.append(cur_path.copy())
  s = required_sum - root.val
  find_all_paths(root.left, s, path_list, cur_path)
  find_all_paths(root.right, s, path_list, cur_path)
  cur_path.pop()


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()


"""
Time O(NlogN)
Space O(NlogN): in a balanced tree, O(N) leaves and O(logN) height
"""

