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
  sum2freq = {0: 1}  # sentinel
  count_p(root, s, 0, sum2freq)
  return cnt 


def count_p(root, s, cur_sum, sum2freq):
  global cnt
  if not root:
    return 
  cur_sum += root.val
  pre_sum = cur_sum - s
  if pre_sum in sum2freq:
    cnt += sum2freq[pre_sum]
  if cur_sum not in sum2freq:
    sum2freq[cur_sum] = 0
  sum2freq[cur_sum] += 1

  count_p(root.left, s, cur_sum, sum2freq)
  count_p(root.right, s, cur_sum, sum2freq)
  sum2freq[cur_sum] -= 1
  if sum2freq[cur_sum] == 0:
    del sum2freq[cur_sum]


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
Time O(N)
Space O(N)
"""

