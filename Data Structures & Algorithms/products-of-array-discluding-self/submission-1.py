class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod=1
        output = [1]*len(nums)
        for i in range(len(nums)):
            output[i] =leftprod
            leftprod *= nums[i]

        rightprod = 1
        for i in range(len(nums)-1,-1,-1):
            output [i] *= rightprod
            rightprod *= nums[i]
        return output