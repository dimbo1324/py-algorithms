class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for idx in range(len(nums)):
            total_sum -= nums[idx]
            if total_sum == left_sum:
                return idx
            left_sum += nums[idx]

        return -1


# ----------------------------------------------


def main():
    solution = Solution()

    nums1 = [1, 7, 3, 6, 5, 6]
    result1 = solution.pivotIndex(nums1)

    nums2 = [1, 2, 3]
    result2 = solution.pivotIndex(nums2)

    nums3 = [2, 1, -1]
    result3 = solution.pivotIndex(nums3)

    nums4 = []
    result4 = solution.pivotIndex(nums4)

    nums5 = [0]
    result5 = solution.pivotIndex(nums5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------

if __name__ == "__main__":
    main()
