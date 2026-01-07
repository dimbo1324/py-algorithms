from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnDict, mgDict = Counter(ransomNote), Counter(magazine)

        for k, v in rnDict.items():
            if v > mgDict[k]:
                return False

        return True


print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
