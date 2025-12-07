class Solution(object):
    def arraySign(self, nums):
        neg_count = 0
        for num in nums:
            if num == 0:
                return 0
            neg_count += num < 0
        return -1 if neg_count % 2 else 1


# ----------------------------------------------
def main():
    nums1 = [-1, -2, -3, -4, 3, 2, 1]
    solution1 = Solution()
    result1 = solution1.arraySign(nums1)
    nums2 = [1, -5, 7, 3, 3, 5]
    solution2 = Solution()
    result2 = solution2.arraySign(nums2)
    nums3 = [2, 8, 7, 3, 6, 7]
    solution3 = Solution()
    result3 = solution3.arraySign(nums3)
    nums4 = [10, 4345, 4333666, 10, 5, 5, 0]
    solution4 = Solution()
    result4 = solution4.arraySign(nums4)
    nums5 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    solution5 = Solution()
    result5 = solution5.arraySign(nums5)
    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
