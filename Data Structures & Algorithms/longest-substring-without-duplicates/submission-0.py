class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l, r = 0, 0
        chars = set()

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
            r += 1
            result = max(result, r - l)
        
        return result