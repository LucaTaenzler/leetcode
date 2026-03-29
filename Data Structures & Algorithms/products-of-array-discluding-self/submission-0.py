class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()

        for num in nums:
            temp = nums.copy()
            temp.remove(num)

            calc = 1
            for t in temp:
                calc *= t
            result.append(calc)

        return result