"""
LC 1481
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.
Example 1:
Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have
to skip 5 because it is not distinct and occurred twice.
Another solution could be to remove one instance of '5' and '3' each to be left with three
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
Example 2:
Input: [3, 5, 12, 11, 12], and K=3
Output: 2
Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then
we can delete any two numbers which will leave us 2 distinct numbers in the result.
Example 3:
Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
Output: 3
Explanation: We can remove one occurrence of '4' to get three distinct numbers.
"""
def find_maximum_distinct_elements(nums, k):
  # freq
  freqs = {}
  for n in nums:
    if n not in freqs:
      freqs[n] = 1
    else:
      freqs[n] += 1
  freqs = bucket_sort(freqs)
  # freq more than 1
  s = freqs[1]  # number of single values
  for freq in range(2, len(freqs)):
    n_val = freqs[freq]
    if n_val * (freq - 1) >= k:
      s += k // (freq - 1)
      return s
    else:
      k -= n_val * (freq - 1)
      s += n_val
  return s - k


def bucket_sort(freqs):
  M = max(freqs.values())
  buckets = [0] * (M + 1)
  for f in freqs.values():
    buckets[f] += 1
  return buckets


def main():
  # 3 2 3 1 4 3

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 6)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 3, 3, 3, 5, 12, 11, 12], 4)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 1)))


main()


"""
Time O(N)
Space O(N)
"""
