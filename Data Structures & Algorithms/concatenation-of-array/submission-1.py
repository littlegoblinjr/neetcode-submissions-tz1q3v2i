class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        ans_length = 2*len(nums)

        n = len(nums)

        

        for _ in range(ans_length):

            ans.append(_)

        for i, v in enumerate(nums):

            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans



        