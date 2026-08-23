class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i in range(len(nums)):
            pairs.append((nums[i],i))
        pairs.sort()
        for i in range(len(pairs)):
            a = pairs[i]
            target2 = target - a[0]
            l=i
            r=len(pairs)
            while(l+1<r):
                mid = (l+r)//2
                b = pairs[mid]
                if(b[0]==target2): return [min(a[1],b[1]),max(a[1],b[1])]
                if(b[0]<target2): l=mid
                if(b[0]>target2): r=mid
                           
    