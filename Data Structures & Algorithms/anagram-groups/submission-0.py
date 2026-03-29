class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        anagrams = list()

        for s in strs:
            key = "".join(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)

        for m in map:
            anagrams.append(map[m])
        return anagrams