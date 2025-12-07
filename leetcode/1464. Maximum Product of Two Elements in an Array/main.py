class Solution(object):
    def maxProduct(self, nums):
        max_1, max_2 = -float("inf"), -float("inf")

        for num in nums:
            if num > max_1:
                max_2, max_1 = max_1, num
            else:
                max_2 = max(num, max_2)

        return (max_2 - 1) * (max_1 - 1)


# ----------------------------------------------


def main():
    solution = Solution()

    nums1 = [3, 4, 5, 2]
    result1 = solution.maxProduct(nums1)

    nums2 = [1, 5]
    result2 = solution.maxProduct(nums2)

    nums3 = [10, 2, 5, 6]
    result3 = solution.maxProduct(nums3)

    nums4 = [5, 5, 5, 5]
    result4 = solution.maxProduct(nums4)

    nums5 = [
        -1,
        -2,
        -3,
        -4,
    ]  # тест с отрицательными — поведение зависит от задачи/ожиданий
    result5 = solution.maxProduct(nums5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------

if __name__ == "__main__":
    main()
