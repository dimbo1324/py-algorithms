from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, w in enumerate(words):
            if x in w:
                ans.append(i)
        return ans


# ----------------------------------------------
def main():
    tests = [
        (["hello", "world", "help", "shell"], "ll"),
        (["apple", "banana", "grape", "pineapple"], "app"),
        (["abc", "def", "ghi"], "x"),
        (["aaaa", "aa", "a"], "aa"),
        (["Case", "case", "CaSe"], "case"),
        ([], "a"),
    ]

    solution = Solution()
    for idx, (words, x) in enumerate(tests, start=1):
        result = solution.findWordsContaining(words, x)
        print(f"Example #{idx} Input: words={words!r}, x={x!r} -> Result: {result}")


# ----------------------------------------------
if __name__ == "__main__":
    main()
