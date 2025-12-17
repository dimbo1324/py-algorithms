from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        target = n * n
        while num <= target:
            for i in range(left, right + 1):
                ans[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                ans[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                ans[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                ans[i][left] = num
                num += 1
            left += 1
        return ans


# ----------------------------------------------
def main():
    tests = [1, 2, 3, 4, 5]
    solution = Solution()

    for idx, n in enumerate(tests, start=1):
        matrix = solution.generateMatrix(n)
        print(f"Example #{idx} (n={n}):")
        for row in matrix:
            print(row)
        print()


# ----------------------------------------------
if __name__ == "__main__":
    main()
