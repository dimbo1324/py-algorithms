class Solution(object):
    def sum(self, num1: int, num2: int) -> int:
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2


# ----------------------------------------------
def main():
    # Example #1 usage:
    solution = Solution()
    num1 = 12
    num2 = 5
    result1 = solution.sum(num1, num2)

    # Example #2 usage:
    num3 = 7
    num4 = 3
    result2 = solution.sum(num3, num4)

    # Example #3 usage:
    num5 = 0
    num6 = 0
    result3 = solution.sum(num5, num6)

    # Example #4 usage:
    num7 = -10
    num8 = 5
    result4 = solution.sum(num7, num8)

    # Example #5 usage:
    num9 = 1000
    num10 = 2000
    result5 = solution.sum(num9, num10)

    # Print results
    print("Example #1: sum({}, {}) = {}".format(num1, num2, result1))
    print("Example #2: sum({}, {}) = {}".format(num3, num4, result2))
    print("Example #3: sum({}, {}) = {}".format(num5, num6, result3))
    print("Example #4: sum({}, {}) = {}".format(num7, num8, result4))
    print("Example #5: sum({}, {}) = {}".format(num9, num10, result5))


# ----------------------------------------------
if __name__ == "__main__":
    main()
