class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seenElements = set()
        
        for i in nums:
            if i in seenElements:
                return True
            seenElements.add(i)
        
        return False
        
        