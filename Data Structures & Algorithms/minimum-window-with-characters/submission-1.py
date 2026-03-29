class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        result = ""
        frequency, window = {}, {}
        l, r = 0, 0

        for c in t:
            frequency[c] = frequency.get(c, 0) + 1
        have, need = 0, len(frequency)

        for char in s:
            window[char] = window.get(char, 0) + 1
            r += 1

            if char in frequency and window[char] == frequency[char]:
                have += 1

            while have == need:
                if (r - l) < len(result) or len(result) == 0:
                    result = s[l:r]
                window[s[l]] -= 1
                if s[l] in frequency and window[s[l]] < frequency[s[l]]:
                    have -= 1
                l += 1

        return result