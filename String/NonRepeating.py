from collections import Counter

class Solution:
    def nonRepeatingChar(self,s):
        freq = Counter(s) #Literally Counts the frequency of a letter occuring!!
        for char in s:
            if freq[char] == 1:
                return char
            else:
                continue
        return '$'