class Solution(object):
    def subtractProductAndSum(self, n):
        a, m = 0, 1
        while n:
            n, d = divmod(n, 10)

            a += d
            m *= d

        return m - a
