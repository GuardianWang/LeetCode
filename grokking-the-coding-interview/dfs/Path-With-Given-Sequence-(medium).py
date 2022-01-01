"""
LC 1430
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  sequence.reverse()
  return find_p(root, sequence)


def find_p(root, sequence):
  if not root or not sequence:  # sequence is too short
    return False
  if root.val != sequence[-1]:
    return False
  if (not root.left) and (not root.right):
    return len(sequence) == 1

  sequence.pop()
  left_find = find_p(root.left, sequence)
  right_find = find_p(root.right, sequence)
  sequence.append(root.val)
  return left_find or right_find


def main():
  # F T
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


"""
Time O(N)
Space O(N)
"""

