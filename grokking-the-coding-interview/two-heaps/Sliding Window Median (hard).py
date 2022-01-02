"""
LC 480
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""
from heapq import *
import heapq


class SlidingWindowMedian:
    def find_sliding_window_median(self, nums, k):
        self.min_heap = []
        self.max_heap = []
        res = []
        for i, n in enumerate(nums):
            self.insert(n)
            if i >= k - 1:
                res.append(self.median())
                self.delete(nums[i - k + 1])
        return res

    def delete(self, n):
        if self.min_heap and self.min_heap[0] <= n:
            heap = self.min_heap
        else:
            heap = self.max_heap
            n = -n
        i = heap.index(n)
        if i == len(heap) - 1:  # the last
            heap.pop()
        else:
            heap[i] = heap.pop()
            heapq._siftup(heap, i)  # move children up
            heapq._siftdown(heap, 0, i)  # move parent down
        self.balance()

    def balance(self):
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.min_heap) < len(self.max_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def insert(self, n):
        if not self.min_heap or self.min_heap[0] <= n:
            heappush(self.min_heap, n)
        else:
            heappush(self.max_heap, -n)
        self.balance()

    def median(self):
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (self.min_heap[0] - self.max_heap[0])
        else:
            return self.min_heap[0]

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()


"""
Time O(NK): find the index takes O(K)
Space O(K)
"""

