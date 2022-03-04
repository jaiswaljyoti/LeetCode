class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<3):
            return 0
        
        ans = 0
        diff = nums[1]-nums[0]
        curr = 1
        for i in range(2, n):
            if(nums[i]-nums[i-1]==diff):
                curr+=1
                if curr>=2:
                    ans+=curr-1
            else:
                diff = nums[i]-nums[i-1]
                curr = 1
        return ans