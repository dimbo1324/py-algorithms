class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        end, ans = n + 1, 0

        for i in range(end):
            if i % m:
                ans += i
            else:
                ans -= i

        return ans


print(Solution().differenceOfSums(10, 3))
