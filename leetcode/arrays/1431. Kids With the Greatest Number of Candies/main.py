class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result


# ----------------------------------------------
def main():
    # Example #1 usage:
    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    solution1 = Solution()
    result1 = solution1.kidsWithCandies(candies1, extraCandies1)

    # Example #2 usage:
    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    solution2 = Solution()
    result2 = solution2.kidsWithCandies(candies2, extraCandies2)

    # Example #3 usage:
    candies3 = [12, 1, 12]
    extraCandies3 = 10
    solution3 = Solution()
    result3 = solution3.kidsWithCandies(candies3, extraCandies3)

    # Example #4 usage:
    candies4 = [5, 6, 2, 3, 1]
    extraCandies4 = 4
    solution4 = Solution()
    result4 = solution4.kidsWithCandies(candies4, extraCandies4)

    # Example #5 usage:
    candies5 = [0, 0, 0]
    extraCandies5 = 0
    solution5 = Solution()
    result5 = solution5.kidsWithCandies(candies5, extraCandies5)

    # Print results
    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------
if __name__ == "__main__":
    main()
