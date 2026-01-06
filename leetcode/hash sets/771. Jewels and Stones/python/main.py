"""
------------------------------
------------------------------

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

------------------------------
------------------------------
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jew_set = set(jewels)
        print(jew_set)

        for s in stones:

            if s in jew_set:
                ans += 1

        return ans


jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))
