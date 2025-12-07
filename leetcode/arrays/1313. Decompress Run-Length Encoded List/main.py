class Solution(object):
    def decompressRLElist(self, nums):
        ans = []
        for i in range(0, len(nums), 2):
            ans += [nums[i + 1]] * nums[i]
        return ans


# ----------------------------------------------
def main():
    nums1 = [1, 2, 3, 4]
    solution1 = Solution()
    result1 = solution1.decompressRLElist(nums1)
    nums2 = [1, 1, 2, 3]
    solution2 = Solution()
    result2 = solution2.decompressRLElist(nums2)
    nums3 = [2, 5]
    solution3 = Solution()
    result3 = solution3.decompressRLElist(nums3)
    nums4 = [4, 7, 1, 9]
    solution4 = Solution()
    result4 = solution4.decompressRLElist(nums4)
    nums5 = [3, 2, 2, 1]
    solution5 = Solution()
    result5 = solution5.decompressRLElist(nums5)
    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
