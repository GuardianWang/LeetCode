"""
LC 703
Design a class to efficiently find the Kth largest element in a stream of numbers.
The class should have the following two things:
The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.
Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
"""
from heapq import *


class KthLargestNumberInStream:

  def __init__(self, k, nums):
    self.k = k
    self.nums = []
    for n in nums:
      self.add_val(n)

  def add(self, val):
    self.add_val(val)
    return self.nums[0]

  def add_val(self, n):
    if len(self.nums) < self.k:
      heappush(self.nums, n)
    elif n > self.nums[0]:
      heapreplace(self.nums, n)


def main():

  kthLargestNumber = KthLargestNumberInStream(nums=[3, 1, 5, 12, 2, 11], k=4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()


"""
Time O(logK): only add()
Space O(K)
"""

