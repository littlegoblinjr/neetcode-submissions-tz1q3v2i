class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        


        
       
        temp = 0
       
        i = 0
        j = len(nums) -1
        
        while i <= j: 
            if nums[i] == val:

                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j = j - 1

            else:
                i = i + 1
           

        return i



            


                

        