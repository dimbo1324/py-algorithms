# from ast import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     ans.extend([i, j])
#         return ans
# nums = [3, 2, 3]
# target = 6
# print(Solution().twoSum(nums, target))


from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in o:
                return [i, o[d]]
            o[nums[i]] = i


nums = [3, 2, 3]
target = 6
print(Solution().twoSum(nums, target))
