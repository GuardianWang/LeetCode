"""
LC 78
Given a set with distinct elements, find all of its distinct subsets.
Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""
def find_subsets(nums):
    # recursive definition:
    # subsets of nums is 
    # subsets of nums[:-1] union subsets concatenating nums[-1]
    res = [[]]
    for n in nums:
        # similar to bfs, use len to iterate the previous layer
        for i in range(len(res)):
            res.append(res[i].copy())
            res[-1].append(n)
    return res


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


"""
Time O(N*2^N)
Space O(N*2^N)
"""

