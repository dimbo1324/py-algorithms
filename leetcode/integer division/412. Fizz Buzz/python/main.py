from ast import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        f, b, fb = "Fizz", "Buzz", "FizzBuzz"

        for i in range(1, n + 1):
            is_f, is_b = i % 3 == 0, i % 5 == 0

            if is_f and is_b:
                ans.append(fb)
            elif is_f:
                ans.append(f)
            elif is_b:
                ans.append(b)
            else:
                ans.append(str(i))
        return ans


n = 1445
print(Solution().fizzBuzz(n))
