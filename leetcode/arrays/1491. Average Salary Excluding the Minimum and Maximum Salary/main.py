class Solution(object):
    def average(self, salary):
        PROPS = {"sum": 0, "len": 0, "min": float("inf"), "max": -float("inf")}

        for val in salary:
            PROPS["sum"] += val
            PROPS["len"] += 1

            if val > PROPS["max"]:
                PROPS["max"] = val

            if val < PROPS["min"]:
                PROPS["min"] = val

        numerator = float(PROPS["sum"] - PROPS["max"] - PROPS["min"])
        denominator = float(PROPS["len"] - 2)
        return numerator / denominator


# ----------------------------------------------


def main():
    solution = Solution()

    salary1 = [4000, 3000, 1000, 2000]
    result1 = solution.average(salary1)

    salary2 = [6000, 5000, 3000, 7000, 4000]
    result2 = solution.average(salary2)

    salary3 = [1500, 1200, 1300, 1100, 1400, 1000]
    result3 = solution.average(salary3)

    salary4 = [10000, 9000, 11000]
    result4 = solution.average(salary4)

    salary5 = [5, 1, 3, 2, 4]
    result5 = solution.average(salary5)

    print("Example #1 Result:", result1)
    print("Example #2 Result:", result2)
    print("Example #3 Result:", result3)
    print("Example #4 Result:", result4)
    print("Example #5 Result:", result5)


# ----------------------------------------------

if __name__ == "__main__":
    main()
