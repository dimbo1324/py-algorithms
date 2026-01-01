# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, m, s = 0, 1, str(n)
        for i in range(len(s)):
            num = int(s[i])
            m *= num
            a += num
        return m - a


n = 234
print(Solution().subtractProductAndSum(n))
