class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        output = []
        for i in range(len(nums)):
            product *= nums[i] if nums[i] != 0 else 1
            if nums[i] == 0: zeros+=1
        if zeros == 0:
            return [product // num for num in nums]
        if zeros == 1:
            return [product if num ==0 else 0 for num in nums]
        return [0] * len(nums)