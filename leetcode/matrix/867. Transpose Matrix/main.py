class Solution(object):
    def transpose(self, matrix):
        # Обработка пустой матрицы или строк без столбцов
        if not matrix or not matrix[0]:
            return []

        new_matrix = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            new_matrix.append(row)

        return new_matrix


# ----------------------------------------------
def main():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    solution1 = Solution()
    result1 = solution1.transpose(matrix1)

    matrix2 = [[1, 2, 3]]
    solution2 = Solution()
    result2 = solution2.transpose(matrix2)

    matrix3 = [[1], [2], [3]]
    solution3 = Solution()
    result3 = solution3.transpose(matrix3)

    matrix4 = []
    solution4 = Solution()
    result4 = solution4.transpose(matrix4)

    matrix5 = [
        [1, 2],
        [3],
    ]
    solution5 = Solution()
    try:
        result5 = solution5.transpose(matrix5)
    except Exception as e:
        result5 = "Error: " + str(e)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
