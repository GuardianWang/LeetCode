"""
LC 744
Given an array of lowercase letters sorted in ascending order,
find the smallest letter in the given array greater than a given ‘key’.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
Write a function to return the next letter of the given ‘key’.
Example 1:
Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:
Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:
Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:
Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""
def search_next_letter(letters, key):
    if key >= letters[-1]:
        return letters[0]
    l, r = 0, len(letters) - 1
    while l <= r:
        m = (l + r) >> 1
        if key < letters[m]:
            r = m - 1
        else:
            l = m + 1
    return letters[l]
    

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()


"""
Time O(logN)
Space O(1)
"""
