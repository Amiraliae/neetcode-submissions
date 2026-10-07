class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(right>left):
                summ=nums[right]+nums[left]+nums[i]
                if(summ==0):
                    output.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -=1
                if(summ>0): right -= 1
                if(summ<0): left += 1
        output = set(output)
        return [list(a) for a in output]
