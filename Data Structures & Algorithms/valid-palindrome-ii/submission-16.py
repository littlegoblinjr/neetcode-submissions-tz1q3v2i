class Solution:
    def validPalindrome(self, s: str) -> bool:



        counter = 0
        i = 0
        j = len(s) - 1

        def greedy_palindrome(start, end):

            while start < end:

                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        
        while i < j:

            if s[i] != s[j]:

                return (greedy_palindrome(i+1, j) or greedy_palindrome(i, j - 1))

            


            i = i + 1
            j = j - 1

        
        return True





                

      

        
        

                