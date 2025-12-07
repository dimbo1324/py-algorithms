class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        num_len = len(nums)
        ans = []
        for idx in range(0, num_len - 3):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            if nums[idx] + nums[idx + 1] + nums[idx + 2] + nums[idx + 3] > target:
                break
            if (
                nums[idx] + nums[num_len - 1] + nums[num_len - 2] + nums[num_len - 3]
                < target
            ):
                continue
            for j in range(idx + 1, num_len - 2):
                if j > idx + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[idx] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[idx] + nums[j] + nums[num_len - 1] + nums[num_len - 2] < target:
                    continue
                left = j + 1
                right = num_len - 1
                while left < right:
                    s = nums[idx] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ans.append([nums[idx], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return ans


# ----------------------------------------------
def main():
    solution = Solution()
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    result1 = solution.fourSum(nums1, target1)
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    result2 = solution.fourSum(nums2, target2)
    nums3 = [0, 0, 0, 0]
    target3 = 0
    result3 = solution.fourSum(nums3, target3)
    nums4 = [-3, -1, 0, 2, 4, 5]
    target4 = 2
    result4 = solution.fourSum(nums4, target4)
    nums5 = [5, -2, -1, 0, 1, 2, -1, -4]
    target5 = 3
    result5 = solution.fourSum(nums5, target5)
    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
