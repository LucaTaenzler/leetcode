class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()

        for i, num in enumerate(nums):
            dif = target - nums[i]
            if dif in table:
                return sorted([i, table[dif]])
            else:
                table[num] = i