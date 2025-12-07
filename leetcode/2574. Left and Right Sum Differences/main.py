class Solution(object):
    def leftRightDifference(self, nums):
        nums = [0] + nums + [0]
        begin = 1
        ans = []

        left_sum = nums[begin - 1]
        right_sum = sum(nums[begin + 1 :])
        ans.append(abs(left_sum - right_sum))

        for i in range(2, len(nums) - 1):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            ans.append(abs(left_sum - right_sum))

        return ans


# ----------------------------------------------


def main():
    solution = Solution()

    nums1 = [10, 4, 8, 3]
    result1 = solution.leftRightDifference(nums1)

    nums2 = [1]
    result2 = solution.leftRightDifference(nums2)

    nums3 = [0, 0, 0, 0]
    result3 = solution.leftRightDifference(nums3)

    nums4 = [5, -2, 3, 7]
    result4 = solution.leftRightDifference(nums4)

    nums5 = []
    result5 = solution.leftRightDifference(nums5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------


if __name__ == "__main__":
    main()
