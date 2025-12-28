class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces, tar = 0, " "
        for i in range(len(s)):
            if s[i] == tar:
                spaces += 1
            if spaces == k:
                return s[:i]
        return s


s = "What is the solution to this problem"
k = 4
print(Solution().truncateSentence(s, k))
