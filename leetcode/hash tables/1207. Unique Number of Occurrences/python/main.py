from typing import Counter
from traitlets import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s, c = Counter(arr), set()
        for v in s.values():
            c.add(v)
        return len(c) == len(s)


arr = [1, 2]
print(Solution().uniqueOccurrences(arr))
