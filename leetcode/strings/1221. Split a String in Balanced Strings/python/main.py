class Solution:
    def balancedStringSplit(self, s: str) -> int: 
        ans = 0
        if s.count("R") == s.count("L"):
            balance = 0
            for c in s:
                if c == "R":
                    balance += 1
                else:
                    balance -= 1
                if balance == 0:
                    ans += 1
        return ans


s = "RLRRLLRLRL"
print(Solution().balancedStringSplit(s))
