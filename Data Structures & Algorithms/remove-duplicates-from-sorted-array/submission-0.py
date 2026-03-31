class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_elements = set()
        temp = 0
        i = 0
        

        for j in range(len(nums)):

            if nums[j] not in unique_elements:

                unique_elements.add(nums[j])
                nums[i] = nums[j]
                i = i + 1



        return len(unique_elements)

        


        