"""
------------------------------
------------------------------

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

------------------------------
------------------------------
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
