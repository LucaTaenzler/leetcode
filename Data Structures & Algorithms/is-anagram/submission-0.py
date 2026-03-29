class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = dict()
        char_count_t = dict()

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        if(char_count_s == char_count_t):
            return True
        else:
            return False