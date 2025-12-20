# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        distance = len(height)
        ans = 0
        if distance > 3:
            # ------------------------------------
            # ------------------------------------
            # left_lim, right_lim = height[0], height[distance - 1]
            for i in range(2, distance):
                dif = abs(height[i] - height[i - 2])
                left, mid, right = height[i - 2], height[i - 1], height[i]

                cond_1: bool = dif == 0 and mid < left and mid < right
                cond_2: bool = left != right
                cond_3: bool = False

                if cond_1:
                    ans += 1

                if cond_2:
                    min_hg = min(left, right)
                    ans += 1
            # ------------------------------------
            # ------------------------------------

        return ans


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# arr = [0, 1, 0, 1]
print(Solution().trap(arr))
