class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        check = {}
        for index, value in enumerate(nums):
            remaining = target - nums[index]
            if remaining in check:
                return sorted([index, check[remaining]])
            
            check[value] = index
       

            
        