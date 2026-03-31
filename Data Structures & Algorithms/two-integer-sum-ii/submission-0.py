class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index_map = {}

        hash_map = {}

        for i,  num in enumerate(numbers):


            index_map[num] = i + 1


        for i, num in enumerate(numbers):

            complement = target - num

            if complement in hash_map:

                return [index_map[complement],index_map[hash_map[complement]]]


            hash_map[num] = complement

        return []



            
        