class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


# ----------------------------------------------
def main():
    matrix1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solution1 = Solution()
    result1 = solution1.isToeplitzMatrix(matrix1)

    matrix2 = [[1, 2], [2, 2]]
    solution2 = Solution()
    result2 = solution2.isToeplitzMatrix(matrix2)

    matrix3 = [[7]]
    solution3 = Solution()
    result3 = solution3.isToeplitzMatrix(matrix3)

    matrix4 = [[1, 2, 3], [4, 1, 2], [5, 4, 1]]
    solution4 = Solution()
    result4 = solution4.isToeplitzMatrix(matrix4)

    matrix5 = [
        [1, 2, 3, 4],
        [5, 1, 9, 3],
        [9, 5, 1, 2],
    ]
    solution5 = Solution()
    result5 = solution5.isToeplitzMatrix(matrix5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
