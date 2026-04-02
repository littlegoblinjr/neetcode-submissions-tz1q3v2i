from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        quantity = Counter(nums).most_common()

        final_list = []
        j = 0

        for key, values in quantity:

            if j < k:

                final_list.append(key)

            else:
                break
            
            j = j + 1

        return final_list

        