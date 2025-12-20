# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        distance = len(height)
        if distance > 3:
            # ------------------------------------
            # ------------------------------------
            # left_lim, right_lim = height[0], height[distance - 1]
            for i in range(2, distance):
                dif = abs(height[i] - height[i - 2])
                left, mid, right = height[i - 2], height[i - 1], height[i]
                delta = 0

                if dif == 0 and mid < left and mid < right:
                    if mid == 0:
                        delta = right
                    else:
                        delta = right - mid

                elif dif != 0 and mid < left and mid < right:
                    min_hg = min(left, right)
                    if mid == 0:
                        delta = min_hg
                    else:
                        delta = min_hg - mid

                ans += delta
            # ------------------------------------
            # ------------------------------------

        return ans


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# arr = [0, 1, 0, 1]
print(Solution().trap(arr))
