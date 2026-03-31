class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        greatest_word = 0
        count = 0
        i = 0
        j = 0
        s = ""
        if len(word1) == len(word2):
            count = len(word1)
        if len(word1) < len(word2):
            count = len(word1)
            greatest_word = word2
        else:
            count = len(word2)
            greatest_word = word1
        
        while i < count and j < count:

            s += word1[i]
            i = i + 1
            s += word2[j]
            j = j + 1

        if len(word1) != len(word2):
            s += greatest_word[count:]

        return s