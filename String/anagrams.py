class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2) -> bool:
        if len(s1) == len(s2):
          a = sorted(s1)
          b = sorted(s2)
          if a == b:
              return True
        else:
            return False