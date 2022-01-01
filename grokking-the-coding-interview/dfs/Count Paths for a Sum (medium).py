"""
LC 437
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


cnt = 0
def count_paths(root, s):
  global cnt 
  count_p(root, s, [])
  return cnt 


def count_p(root, s, sums):
  global cnt
  if not root:
    return 
  # add root.val 
  sums.append(0)
  for i in range(len(sums)):
    sums[i] += root.val 
    if sums[i] == s:
      cnt += 1
  
  count_p(root.left, s, sums)
  count_p(root.right, s, sums)
  sums.pop()
  for i in range(len(sums)):
    sums[i] -= root.val 


def main():
  # 2
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()


"""
Time O(N^2) O(NlogN)
Space O(N)
"""

