class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
# nums = [1,2,3,4]
        
        i = 0  
        
        for i in range(len(nums)-1):
            j = i + 1
            if nums[i] == nums[j]:
                return True
            j += 1
            i += 1
        return False