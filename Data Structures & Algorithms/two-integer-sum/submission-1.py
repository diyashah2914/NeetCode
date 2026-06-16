class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # Pseudo-Code:

        # loop through the list
        for i in range(len(nums)-1):
            # Have a nested inner loop
            for j in range(len(nums)):
                # add the the number in outer loop with the number in inner loop
                # check if their addition ==  target
                # and check if i != j
                if i != j and nums[i] + nums[j] == target:
                    text = [i,j]
                    # break
                    return text
                else:
                    j += 1
            i += 1
                    

        
        
       


    
                
             