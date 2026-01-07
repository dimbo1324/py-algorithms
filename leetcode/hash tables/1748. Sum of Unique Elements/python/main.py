"""
------------------------------
------------------------------

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

------------------------------
------------------------------
"""

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d, ans = {}, 0
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for k, v in d.items():
            if v == 1:
                ans += k
        return ans


nums = [1, 2, 3, 2]
print(Solution().sumOfUnique(nums))
