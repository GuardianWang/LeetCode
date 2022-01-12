"""
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
Example 1:
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
Example 2:
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}
Example 3:
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
"""
def can_partition(nums, s):
  num_sum = sum(nums)
  if s > num_sum:
    return False
  elif s == num_sum:
    return True

  dp = [False] * (s + 1)
  dp[0] = True

  for n in nums:
    if n > s:
      continue
    elif n == s:
      return True
    for i in range(s, n - 1, -1):
      dp[i] = dp[i] or dp[i - n]
    if dp[s]:
      return True
  return False


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()


"""
Time O(NC): don't need to sort by weight
Space O(C)
"""
