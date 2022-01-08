"""
LC 90
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
"""
def find_subsets(nums):
    # sort the array and group duplicates together
    nums.sort()

    res = [[]]
    for i, n in enumerate(nums):
        # when there are duplicates, only add the last several ndoes
        if i == 0 or n != nums[i - 1]:
            append_len = len(res)
        for j in range(len(res) - append_len, len(res)):
            res.append(res[j].copy())
            res[-1].append(n)

    return res


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()


"""
Time O(N*2^N)
Space O(N*2^N)
"""
