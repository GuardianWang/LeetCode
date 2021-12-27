"""
LC 457
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example 1:

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
Example 2:

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
Example 3:

Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.
"""


def circular_array_loop_exists(arr):
    slow, fast = 0, 0
    
    visited = set()
    # this is guaranteed to have cycles,
    # but need to check if cycle is legal
    for i in range(len(arr)):  # can start anywhere
        if i in visited:
            continue
        slow, fast = i, i
        while True:
            visited.add(i)
            slow = next_id(arr, slow)
            visited.add(slow)
            if ((arr[i] > 0) != (arr[slow] > 0)):
                break
            fast = next_id(arr, fast)
            visited.add(fast)
            if ((arr[i] > 0) != (arr[fast] > 0)):
                break  # different direction
            fast = next_id(arr, fast)
            visited.add(fast)
            if ((arr[i] > 0) != (arr[fast] > 0)):
                break  # different direction

            if slow == fast:
                if next_id(arr, slow) == slow:
                    break  # only 1 element
                return True
    return False


def next_id(arr, i):
    return (i + arr[i]) % len(arr)

def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))  # T
  print(circular_array_loop_exists([2, 2, -1, 2]))  # T
  print(circular_array_loop_exists([2, 1, -1, -2]))  # F
  print(circular_array_loop_exists([1, 1, 4, -2]))  # F


main()


"""
Time O(N)
Space O(N)
"""
