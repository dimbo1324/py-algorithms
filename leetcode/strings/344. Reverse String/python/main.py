from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


s = ["h", "e", "l", "l", "o"]
Solution().reverseString(s)
# print(s)
