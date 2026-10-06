class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod=1
        output = []
        for i in range(len(nums)):
            output.append(leftprod)
            leftprod *= nums[i]

        rightprod = 1
        for i in range(len(nums)-1,-1,-1):
            output [i] *= rightprod
            rightprod *= nums[i]
        return output