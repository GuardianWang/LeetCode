# Problems

## [Tiktok](https://www.1point3acres.com/bbs/thread-850692-1-1.html)

1. [Reaching Points (Hard)](Reaching-Points-(Hard).py)
[[LC780](https://leetcode.com/problems/reaching-points/)]
1. [Stars and Bars](Stars-and-Bars.py)
[[link](https://leetcode.com/discuss/interview-question/1748177/ByteDance-(TikTok)-OA-or-FTE-or-University-Hiring-(USA))]
1. [Find Size 3 Inversions in a list](Find-Size-3-Inversions-in-a-list.py)
[[link](https://leetcode.com/discuss/interview-question/777188/find-size-3-inversions-in-a-list)]
1. [Ancestral Names](Ancestral-Names.py)
[[link](https://leetcode.com/discuss/general-discussion/851939/ancestor-problem)]
1. [Design a Stack With Increment Operation (Medium)](Design-a-Stack-With-Increment-Operation-(Medium).py)
[[LC1381](https://leetcode.com/problems/design-a-stack-with-increment-operation/)]
<!--
2. [Unique Paths (Medium)](Unique-Paths-(Medium).py)
[[LC62](https://leetcode.com/problems/unique-paths/)]
3. [Number of Sets of K Non-Overlapping Line Segments (Medium)](Number-of-Sets-of-K-Non-Overlapping-Line-Segments-(Medium).py)
[[LC1621](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)]
4. [Global and Local Inversions (Medium)](Global-and-Local-Inversions-(Medium).py)
[[LC775](https://leetcode.com/problems/global-and-local-inversions/)]
-->

## [Tiktok](https://www.1point3acres.com/bbs/thread-850122-1-1.html)

1. [Design a Stack With Increment Operation (Medium)](Design-a-Stack-With-Increment-Operation-(Medium).py)
[[LC1381](https://leetcode.com/problems/design-a-stack-with-increment-operation/)]
1. [Circular Printer](Circular-Printer.py)
[[link](https://leetcode.com/discuss/interview-question/1263982/thomson-reuters-oa-circular-printer)]
1. [Lexicographically smallest and largest substring of size k (Medium)](Lexicographically-smallest-and-largest-substring-of-size-k-(Medium).py)
[[link](https://www.geeksforgeeks.org/lexicographically-smallest-and-largest-substring-of-size-k/)]
1. [Ancestral Names](Ancestral-Names.py)
[[link](https://leetcode.com/discuss/general-discussion/851939/ancestor-problem)]
1. [Count of Smaller Numbers After Self (Hard)](Count-of-Smaller-Numbers-After-Self-(Hard).py)
[[LC315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)]
1. [Find Size 3 Inversions in a list](Find-Size-3-Inversions-in-a-list.py)
[[link](https://leetcode.com/discuss/interview-question/777188/find-size-3-inversions-in-a-list)]

## [Tiktok](https://leetcode.com/discuss/interview-question/1710950/TikTok-OA-2022.1.22)
1. [Reaching Points (Hard)](Reaching-Points-(Hard).py)
[[LC780](https://leetcode.com/problems/reaching-points/)]
1. [Smallest Subarray with a given sum (easy)](Smallest-Subarray-with-a-given-sum-(easy).py)
[[LC209](https://leetcode.com/problems/minimum-size-subarray-sum)]
1. [Dominos Tiling 3D](Dominos-Tiling-3D.py)
[[link](https://www.1point3acres.com/bbs/thread-835608-1-1.html)]
1. [Reformat Date (Easy)](Reformat-Date-(Easy).py)
[[LC1507](https://leetcode.com/problems/reformat-date/)]
1. [Shared Interest](Shared-Interest.py)
[[link](https://leetcode.com/discuss/interview-question/725801/amazon-shared-interest-problem)]

## [Verkada](https://www.1point3acres.com/bbs/thread-810255-1-1.html)
1. [First Unique Character in a String (Easy)](First-Unique-Character-in-a-String-(Easy).py)
[[LC387](https://leetcode.com/problems/first-unique-character-in-a-string/)]
1. [Check if Array Is Sorted and Rotated (Easy)](Check-if-Array-Is-Sorted-and-Rotated-(Easy).py)
[[LC1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)]
1. [Subarray With Unique Elements](Subarray-With-Unique-Elements.py)
[[link](https://www.1point3acres.com/bbs/thread-810255-1-1.html)]

## [Verkada](https://www.1point3acres.com/bbs/thread-811988-1-1.html)
1. [Construct K Palindrome Strings (Medium)](Construct-K-Palindrome-Strings-(Medium).py)
[[LC1400](https://leetcode.com/problems/construct-k-palindrome-strings/)]
1. [Merge Two Sorted Lists (Easy)](Merge-Two-Sorted-Lists-(Easy).py)
[[LC21](https://leetcode.com/problems/merge-two-sorted-lists/)]

1. []()
[[]()]

# Tricks

1. [stars and bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics))
2. [binary index tree](https://www.youtube.com/watch?v=WbafSgetDDk) 
- idx starts from 1
- update: idx += idx & -idx
- query: idx -= idx & -idx
3. bisect: think of arr = [0, 1]
- `bisect_right(arr, 0) == 1`
- `bisect_left(arr, 0) == 0`
- `max(bisect_right(arr, v) - 1, 0)` closest value <= v
- `min(bisect_left(arr, v), len(arr) - 1)` closest value >= v
4. `min(generator, default=v)` default
5. `(i for i in range(3))` in `()` is a generator
