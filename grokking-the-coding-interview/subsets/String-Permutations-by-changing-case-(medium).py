'''
LC 784
Problem Statement
Given a string, find all of its permutations preserving the character sequence but changing case.
Example 1:
Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:
Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''
def find_letter_case_string_permutations(s):
    ans = [s]
    for i, c in enumerate(s):
        if c.isalpha():
            for j in range(len(ans)):
                new_s = list(ans[j])
                new_s[i] = new_s[i].swapcase()
                ans.append("".join(new_s))
    return ans


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()


"""
Time O(N*2^N)
Space O(N*2^N)
"""
