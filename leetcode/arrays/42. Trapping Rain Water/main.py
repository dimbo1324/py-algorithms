from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        distance = len(height)
        if distance >= 3:
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
        return ans


# ----------------------------------------------
def main():
    tests = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [2, 0, 2],
        [0, 0, 0, 0],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 0, 0, 2, 0, 4],
        [1],
        [],
    ]
    solution = Solution()
    for idx, h in enumerate(tests, start=1):
        result = solution.trap(h)
        print(f"Example #{idx} Input: {h} -> Trapped: {result}")


# ----------------------------------------------
if __name__ == "__main__":
    main()
