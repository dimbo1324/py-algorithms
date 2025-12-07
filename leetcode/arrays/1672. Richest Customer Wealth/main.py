class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(customer) for customer in accounts])


# ----------------------------------------------
def main():
    # Example #1 usage:
    accounts1 = [[1, 2, 3], [3, 2, 1]]
    solution1 = Solution()
    result1 = solution1.maximumWealth(accounts1)

    # Example #2 usage:
    accounts2 = [[1, 5], [7, 3], [3, 5]]
    solution2 = Solution()
    result2 = solution2.maximumWealth(accounts2)

    # Example #3 usage:
    accounts3 = [[2, 8, 7], [3, 6, 7]]
    solution3 = Solution()
    result3 = solution3.maximumWealth(accounts3)

    # Example #4 usage:
    accounts4 = [[10, 0], [0, 10], [5, 5]]
    solution4 = Solution()
    result4 = solution4.maximumWealth(accounts4)

    # Example #5 usage:
    accounts5 = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
    solution5 = Solution()
    result5 = solution5.maximumWealth(accounts5)

    # Print results
    print("Example #1 Result:", result1)  # Expected Output: 6
    print("Example #2 Result:", result2)  # Expected Output: 10
    print("Example #3 Result:", result3)  # Expected Output: 17
    print("Example #4 Result:", result4)  # Expected Output: 10
    print("Example #5 Result:", result5)  # Expected Output: 6


# ----------------------------------------------
if __name__ == "__main__":
    main()
