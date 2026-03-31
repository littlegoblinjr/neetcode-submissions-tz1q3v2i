class Solution:
    def isPalindrome(self, s: str) -> bool:

        word = ""

        for i, letter in enumerate(s):

            if letter.isalnum():

                word = word + letter.lower()

        i = 0
        j = len(word) - 1

        while i <= j:

            if word[i] != word[j]:

                return False

            i = i  + 1

            j = j - 1

        return True

        