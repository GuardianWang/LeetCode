"""
LC 6014
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
"""
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = dict(Counter(s))
        cs = sorted(cnt)
        ans = []
        # print(cnt, cs)
        while cs:
            self.use_letter(cnt, cs, ans, repeatLimit)
            # print(ans)
            
        return "".join(ans)
        
    def use_letter(self, cnt, cs, ans, repeatLimit):
        c = cs[-1]
        while True:
            app_n = min(repeatLimit, cnt[c])
            ans.append(c * app_n)
            cnt[c] -= app_n
            if cnt[c] > 0 and len(cs) > 1:
                backup = cs[-2]
                ans.append(backup)
                cnt[backup] -= 1
                if cnt[backup] == 0:
                    cs.pop(len(cs) - 2)
            else:
                break
            
        cs.pop()
        
        
"""
Time/Space O(N)
"""        

