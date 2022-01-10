"""
LC 451
Given a string, sort it based on the decreasing frequency of its characters.
Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""
def sort_character_by_frequency(s):
  # freq 
  freqs = {}
  for c in s:
    if c not in freqs:
      freqs[c] = 1
    else:
      freqs[c] += 1
  # sort 
  freqs = [(c, f) for c, f in freqs.items()]
  freqs.sort(key=lambda x: -x[1])
  # reconstruct
  return "".join([c * f for c, f in freqs])


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()


"""
Time O(NlogN)
Space O(N)
"""

