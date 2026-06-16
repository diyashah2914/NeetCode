class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # Pseudo-Code:

        # loop through the list
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    text = [i,j]
                    return text
                else:
                    j += 1
            i += 1
                    

        # Have a nested inner loop
        # add the the number in outer loop with the number in inner loop
        # check if their addition ==  target
        # break


        # seen = set()
        # output = list()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output.append([i,j])

                
             