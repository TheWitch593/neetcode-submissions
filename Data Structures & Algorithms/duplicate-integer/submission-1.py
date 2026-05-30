class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
     number = len(nums)
     temp = len(set(nums))
    
     return number != temp