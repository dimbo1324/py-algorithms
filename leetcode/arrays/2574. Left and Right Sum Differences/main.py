class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        ans = []
        for x in nums:
            total -= x
            ans.append(abs(left - total))
            left += x
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
