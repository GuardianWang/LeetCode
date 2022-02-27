"""
https://leetcode.com/playground/GH6hE6Yi

Construct 2 subarraries of the same length with unique values.
"""
def split_subarray(nums):
    cnt = Counter(nums)
    if max(cnt.values()) > 2:
        return [] 
    arr1, arr2 = [], []
    target_len = len(nums) >> 1
    # first fill in repeated values
    for n, freq in cnt.items():
        if freq == 1:
            continue
        arr1.append(n)
        arr2.append(n)
    for n, freq in cnt.items():
        if freq == 2:
            continue
        if len(arr1) < target_len:
            arr1.append(n)
        else:
            arr2.append(n)
            
    return arr1, arr2


nums = [1,2,3,4,5,6,7,7]
print(split_subarray(nums))
nums = [1,1,1,2]
print(split_subarray(nums))
    

"""
Time/Space O(N)
"""
