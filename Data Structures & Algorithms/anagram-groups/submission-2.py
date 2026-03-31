from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hash_table = defaultdict(list)

        for word in strs:

            key = ''.join(sorted(word))

            hash_table[key].append(word)

        return list(hash_table.values())
        