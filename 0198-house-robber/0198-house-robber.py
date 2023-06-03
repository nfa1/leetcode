class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        maxAmount = [0] * n
        maxAmount[0] = nums[0]
        maxAmount[1] = max(nums[0], nums[1])
        
        for i in range (2, n):
            maxAmount[i] = max(maxAmount[i-1],maxAmount[i-2] + nums[i])
    
        return maxAmount[n-1]
    
            