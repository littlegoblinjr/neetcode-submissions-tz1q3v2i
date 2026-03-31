from collections import Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        freq_map = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, freq in freq_map.items():

            buckets[freq].append(key)


        for i in range(len(buckets) - 1, 0, -1):

            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results

                


