class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans, charts_cnt = 0, Counter(chars)

        for w in words:
            ans += len(w) if charts_cnt >= Counter(w) else 0

        return ans