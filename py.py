# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        distance = len(height)
        if distance > 3:
            # ------------------------------------
            # ------------------------------------
            lt, rg = 0, distance - 1
            lt_max, rg_max = 0, 0
            while lt <= rg:
                if height[lt] <= height[rg]:
                    if height[lt] >= lt_max:
                        lt_max = height[lt]
                    else:
                        ans += lt_max - height[lt]

                    lt += 1

                else:
                    if height[rg] >= rg_max:
                        rg_max = height[rg]
                    else:
                        ans += rg_max - height[rg]

                    rg -= 1

            # ------------------------------------
            # ------------------------------------

        return ans


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# arr = [0, 1, 0, 1]
print(Solution().trap(arr))
