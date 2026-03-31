class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char1_set = sorted(s)
        char2_set = sorted(t)


        for i , v in enumerate(char1_set):

            if char1_set[i] == char2_set[i]:
                continue
            else:
                return False
        return True