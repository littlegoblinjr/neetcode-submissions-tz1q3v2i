class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = len(nums) - 1
        
        k = 0

        for i, element in enumerate(nums):

            if nums[i] != val:

                nums[k] = nums[i]

                k = k + 1

        return k




        