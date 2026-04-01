class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        return self.merge_sort(nums)

    

    def merge_sort(self, nums):

        if len(nums) == 1:
            return nums

        mid = len(nums)//2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        result = []

        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                result.append(left[i])

                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result


        