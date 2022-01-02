"""
LC 295
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""
from heapq import *


class MedianOfAStream:
    def __init__(self):
        self.min_heap = []  # large half, including the middle 
        self.max_heap = []  # small half 
    
    def insert_num(self, num):
        # to make a max heap, negate all numbers
        if not self.min_heap or self.min_heap[0] <= num:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        # self.max_heap[0] <= self.min_heap[0] and
        # len(self.max_heap) == len(self.min_heap) or 
        # len(self.max_heap) == len(self.min_heap) - 1
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.min_heap) < len(self.max_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        print(self.max_heap, self.min_heap)

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (self.min_heap[0] + -self.max_heap[0])
        else:
            return self.min_heap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()


"""
Time insert O(logN), find O(1)
Space O(N)
"""

