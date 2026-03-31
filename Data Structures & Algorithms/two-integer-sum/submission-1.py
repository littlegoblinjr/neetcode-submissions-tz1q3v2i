class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        for i, element in enumerate(nums):
            result = target - nums[i]

            if result in hash_map:
                return sorted([hash_map[result], i])

            
            hash_map[nums[i]] = i

            i = i + 1