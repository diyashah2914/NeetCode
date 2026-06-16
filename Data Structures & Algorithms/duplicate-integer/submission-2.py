class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = input().split()

        i = 0
        j = 0
        for i in nums:
            for j in nums:
                if nums[i] == nums[j]:
                    return true
                    j += 1
            i += 1
        return false