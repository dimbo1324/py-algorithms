from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans: List[int] = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


# ----------------------------------------------
def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution1 = Solution()
    result1 = solution1.spiralOrder(matrix1)

    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    solution2 = Solution()
    result2 = solution2.spiralOrder(matrix2)

    matrix3 = [[1, 2, 3, 4]]
    solution3 = Solution()
    result3 = solution3.spiralOrder(matrix3)

    matrix4 = [[1], [2], [3], [4]]
    solution4 = Solution()
    result4 = solution4.spiralOrder(matrix4)

    matrix5 = [[7]]
    solution5 = Solution()
    result5 = solution5.spiralOrder(matrix5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
