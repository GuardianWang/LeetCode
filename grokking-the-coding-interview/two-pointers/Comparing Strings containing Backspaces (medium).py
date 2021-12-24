"""
LC 844
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""


def backspace_compare(str1, str2):
    # delete letter from right to left
    # so pointer begins from right
    p1, p2 = len(str1) - 1, len(str2) - 1
    while p1 >= 0 and p2 >= 0:
        # move to letter
        if str1[p1] == '#':
            cnt = 0
            while str1[p1] == '#':
                p1 -= 1
                cnt += 1
            p1 -= cnt 
        if str2[p2] == '#':
            cnt = 0
            while str2[p2] == '#':
                p2 -= 1
                cnt += 1
            p2 -= cnt 
        # check
        if str1[p1] != str2[p2]:
            return False
        else:
            p1 -= 1
            p2 -= 1
    return p1 < 0 and p2 < 0


def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()


"""
Time O(N)
Space O(1)
"""

