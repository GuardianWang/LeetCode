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
  freqs = bucket_sort(freqs)
  # reconstruct
  return "".join([c * f for c, f in freqs])


def bucket_sort(freqs):
  # Time O(N)
  # Space O(N)
  buckets = [[] for _ in range(1 + max(map(lambda x: x[1], freqs)))]
  for c, f in freqs:
    buckets[f].append(c)
  freqs = []
  for i in range(len(buckets) - 1, -1, -1):
    x = buckets[i]
    if len(x) > 0:
      freqs.extend([(c, i) for c in x])
  return freqs


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()


"""
Time O(N)
Space O(N)
"""

