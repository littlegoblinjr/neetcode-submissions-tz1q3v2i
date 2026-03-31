class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == " ":
            return True

        s = ''.join(c for c in s if c.isalnum()).lower()
         

        i = 0
        j = len(s) - 1

        while i <= j:

            if s[i] == s[j]:
                i = i + 1
                j = j - 1
                
            else:
                return False

           

        return True