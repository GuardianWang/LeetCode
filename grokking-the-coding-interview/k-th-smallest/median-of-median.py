"""
LC 215
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].
Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""
def find_Kth_smallest_number(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        p = partition(nums, l, r)
        if p < k - 1:
            l = p + 1
        else:
            r = p
    return nums[l]


def partition(nums, l, r):
    p  = mom(nums, l, r)
    swap(nums, p, r)
    for i in range(l, r):
        if nums[i] < nums[r]:
            swap(nums, l, i)
            l += 1
    swap(nums, l, r)
    return l


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


def mom(nums, l, r):
  n = high - low + 1
  # if we have less than 5 elements, ignore the partitioning algorithm
  if n < 5:
    return nums[low]

  # partition the given array into chunks of 5 elements
  partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

  # for simplicity, lets ignore any partition with less than 5 elements
  fullPartitions = [
    partition for partition in partitions if len(partition) == 5]

  # sort all partitions
  sortedPartitions = [sorted(partition) for partition in fullPartitions]

  # find median of all partations; the median of each partition is at index '2'
  medians = [partition[2] for partition in sortedPartitions]

  return partition(medians, 0, len(medians)-1)


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()


"""
Time O(N) 
Space O(N)
"""
