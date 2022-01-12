"""
LC 1049
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
Example 1:
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2:
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3:
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""
def can_partition(nums):
  num_sum = sum(nums)
  s = num_sum >> 1
  prev = [False] * (s + 1)
  prev[0] = True
  cur = prev.copy()
  M = 0
  for n in nums:
    if n > s:
      continue
    elif n == s:
      return num_sum - 2 * s

    for i in range(n, len(cur)):
      cur[i] = prev[i] or prev[i - n]
      if cur[i]:
        M = max(M, i)

    if cur[s]:
      return num_sum - 2 * s
    prev = cur.copy()

  return num_sum - 2 * M


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()


"""
Time O(NC): don't need to sort by weight
Space O(C)
"""
