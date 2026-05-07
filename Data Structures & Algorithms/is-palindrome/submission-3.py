class Solution:
    def isPalindrome(self, s: str) -> bool:

        joined_s = ''.join(char.lower() for char in s if char.isalnum())

        i = 0
        j = len(joined_s) - 1


        while i <= j:

            if joined_s[i] != joined_s[j]:
                return False

            i = i + 1
            j = j - 1

        return True
        