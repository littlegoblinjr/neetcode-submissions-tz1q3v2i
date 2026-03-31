class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        result = []

        for i, element in enumerate(nums):

            complement = target - element

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[element] = i

        return []

            

                

        

        return False



        