class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = dict()
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        result, temp = 0, 1

        for key in hashmap:
            if (key - 1) not in hashmap:
                i = 1
                while (key + i) in hashmap:
                    temp += 1
                    i += 1
                if temp > result:
                    result = temp
                temp = 1
        
        return result