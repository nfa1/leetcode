class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # initialize an empty set
        seen_elements = set()
        
        # iterate through the list
        for num in nums: 
            if num in seen_elements:
                return True # Duplicate found
            seen_elements.add(num) # add element to hash set
        return False # No duplicates found
    
        