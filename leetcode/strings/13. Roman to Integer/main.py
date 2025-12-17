class Solution:
    def romanToInt(self, s: str) -> int:
        D = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        n = len(s)
        for i, ch in enumerate(s):
            if i + 1 < n and D[ch] < D[s[i + 1]]:
                total -= D[ch]
            else:
                total += D[ch]
        return total


# ----------------------------------------------
def main():
    tests = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV",
        "CMXCIX",
        "MMXXV",
        "XL",
        "CD",
    ]

    solution = Solution()
    for idx, s in enumerate(tests, start=1):
        result = solution.romanToInt(s)
        print(f"Example #{idx} Input: {s} -> Result: {result}")


# ----------------------------------------------
if __name__ == "__main__":
    main()
