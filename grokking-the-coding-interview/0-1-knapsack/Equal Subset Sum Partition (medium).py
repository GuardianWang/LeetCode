"""
LC 416
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
Example 1:
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
"""
def can_partition(nums):
  s = sum(nums)
  if s % 2 == 1:
    return False
  half = s // 2
  dp = [False] * (half + 1)
  dp[0] = True  # empty set
  for n in nums:
    if n > half:
      continue
    elif n == half:
      return True
    for i in range(half, n - 1, -1):
      dp[i] = dp[i] or dp[i - n]
    if dp[-1]:
      return True
  return False


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))  # F


main()


"""
Time O(NC): don't need to sort by weight
Space O(C)
"""
