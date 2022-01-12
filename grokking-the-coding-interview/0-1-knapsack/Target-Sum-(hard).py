"""
LC 494
You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
Example 1:
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
Example 2:
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
"""
def find_target_subsets(nums, s):
  # split into 2 set, difference is s
  num_sum = sum(nums)
  small_double = num_sum - abs(s)
  if small_double < 0 or small_double % 2:
    return 0
  small = small_double >> 1  # smaller sum
  dp = [0] * (small + 1)
  dp[0] = 1
  for n in nums:
    if n > small:
      continue
    for i in range(small, n - 1, -1):
      dp[i] += dp[i - n]
  return dp[-1]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()


"""
Time O(NC): don't need to sort by weight
Space O(C)
"""
