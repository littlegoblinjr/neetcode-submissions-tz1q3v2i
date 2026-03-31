class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_word = min(strs, key = len)

        prefix = ""

        for i, ch in  enumerate(shortest_word):

            for j in strs:

                if j[i] != ch:

                    return prefix

            prefix = prefix + ch
                    
        
        return prefix



        