"""
------------------------------
------------------------------

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

------------------------------
------------------------------
"""

from typing import Counter, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans, charts_cnt = 0, Counter(chars)

        for w in words:
            ans += len(w) if charts_cnt >= Counter(w) else 0

        return ans


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(Solution().countCharacters(words, chars))
