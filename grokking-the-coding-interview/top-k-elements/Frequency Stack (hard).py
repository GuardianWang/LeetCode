"""
LC 895
Design a class that simulates a Stack data structure, implementing the following two operations:
push(int num): Pushes the number ‘num’ on the stack.
pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.
Example:
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
 
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
"""
from heapq import *


class FrequencyStack:
  def __init__(self):
    self.stack = []
    self.n2freqs = {}
    self.cnt = 0

  def push(self, num):
    if num in self.n2freqs:
      self.n2freqs[num] += 1
    else:
      self.n2freqs[num] = 1
    heappush(self.stack, [-self.n2freqs[num], -self.cnt, num])
    self.cnt += 1

  def pop(self):
    n = heappop(self.stack)[2]
    self.n2freqs[n] -= 1
    return n


def main():
  # 2 1 2 5 3 2
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()


"""
Time O(logN)
Space O(N)
"""

