class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        frequency = dict()
        maxf = 0
        result = 0

        while r < len(s):
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            maxf = max(frequency.values())

            if (r - l + 1) - maxf <= k:
                result = max(result, r - l + 1)
            else:
                while (r - l + 1) - maxf > k:
                    frequency[s[l]] -= 1
                    l += 1
                    maxf = max(frequency.values())
            r += 1


        return result