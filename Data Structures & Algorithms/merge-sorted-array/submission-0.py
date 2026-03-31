class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]

        for j in range(1, len(nums1)):
            key = nums1[j]
            i = j - 1

            while i >= 0 and key<nums1[i]:

                nums1[i + 1] = nums1[i]
                i = i - 1
            
            nums1[i + 1] = key
