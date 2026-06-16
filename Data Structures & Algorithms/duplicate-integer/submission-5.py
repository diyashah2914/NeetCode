class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        if len(nums) >= 0  and len(nums) <= 10**5:
            for k in range(len(nums)):
                if nums[k] >= -10**9 and nums[k] <= 10**9:
                    for i in range(len(nums)-1):
                        for j in range(i+1, len(nums)):
                            if nums[i] == nums[j]:
                                return True
                            j += 1 
                        i += 1
                    return False
            k += 1
        
        

