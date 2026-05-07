class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        length = len(word1)

        if len(word1) < len(word2):

            length = len(word1)

        else:
            length = len(word2)

        i= 0
        
        s = ""
        while i < length:

            s += word1[i]
            s += word2[i]

            i = i + 1


        if len(word1) < len(word2):

            return s + word2[length: len(word2)]

        else:
            return s + word1[length: len(word1)]

        return s



        