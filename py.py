# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        distance = len(height)
        right_lim = height[distance - 1]

        if distance > 3:
            # ------------------------------------
            # ------------------------------------
            for i in range(2, distance):
                dif = abs(height[i] - height[i - 2])
                left, mid, right = height[i - 2], height[i - 1], height[i]
                delta = 0
                is_pit = mid < left and mid < right
                is_hill = mid > left and mid > right

                if is_pit:
                    if dif == 0:
                        if mid == 0:
                            delta = right
                        else:
                            delta = right - mid
                    else:
                        min_hg = min(left, right)
                        if mid == 0:
                            delta = min_hg
                        else:
                            delta = min_hg - mid

                elif is_hill:
                    delta = 0

                else:
                    if mid > right and right_lim > 0:
                        begin = i + 1
                        count = 1
                        if begin < distance:
                            delta = 1
                            for j in range(begin, distance):
                                if height[j] == right:
                                    delta += 1
                                elif height[j] > right:
                                    delta = 1 if delta < 2 else delta
                                    break

                ans += delta
            # ------------------------------------
            # ------------------------------------

        return ans


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# arr = [0, 1, 0, 1]
print(Solution().trap(arr))
