"""
Count of Subset Sum (hard)
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
Example 1: #
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2: #
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
"""
def count_subsets(num, s):
  num_sum = sum(num)
  if num_sum < s:
    return 0
  elif num_sum == s:
    return 1

  prev = [0] * (s + 1)
  prev[0] = 1  # empty
  cur = prev.copy()
  for n in num:
    if n > s:
      continue
    for i in range(n, len(cur)):
      cur[i] = prev[i] + prev[i - n]
    prev = cur.copy()
  return cur[-1]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()


"""
Time O(NC): don't need to sort by weight
Space O(C)
"""
