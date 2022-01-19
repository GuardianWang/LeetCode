"""
LC 287
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""


def find_duplicate(nums):
    # don't modify nums
    # duplicates will form a cycle of length < len(nums)
    # a1 will point to b, b goes to a2, a2 points to b again
    # duplicate number will be at the start of cycle as id

    # two pointers
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break 
    # length 
    cnt = 0
    while True:
        slow = nums[slow]
        cnt += 1
        if slow == fast:
            break 
    # start 
    slow, fast = 0, 0
    for _ in range(cnt):
        fast = nums[fast]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()


"""
Time O(N)
Space O(1)
"""

