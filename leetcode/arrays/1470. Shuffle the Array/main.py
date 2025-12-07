class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.extend([nums[i], nums[n + i]])
        return ans


# ----------------------------------------------
def main():
    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    solution1 = Solution()
    result1 = solution1.shuffle(nums1, n1)
    nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
    n2 = 4
    solution2 = Solution()
    result2 = solution2.shuffle(nums2, n2)
    nums3 = [1, 1, 2, 2]
    n3 = 2
    solution3 = Solution()
    result3 = solution3.shuffle(nums3, n3)
    nums4 = [1, 2, 3, 4, 4, 3, 2, 1]
    n4 = 4
    solution4 = Solution()
    result4 = solution4.shuffle(nums4, n4)
    nums5 = [1, 2, 3, 4, 4, 3, 2, 1]
    n5 = 4
    solution5 = Solution()
    result5 = solution5.shuffle(nums5, n5)
    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
