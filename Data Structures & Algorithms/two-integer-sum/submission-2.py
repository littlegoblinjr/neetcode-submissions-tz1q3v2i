class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i , element in enumerate(nums):

            lookup = target - nums[i]
            if lookup in hash_table:

                return [hash_table[lookup], i]

            else:

                hash_table[nums[i]] = i
        