class Solution:
    def computeLPS(self,pat):
        m = len(pat)
        lps = [0] * m
        length = 0 
        i = 1
        
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length 
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    def minChar(self, s):
        rev = s[::-1]
        temp = s + '#' + rev
        lps = self.computeLPS(temp)
        return len(s) - lps[-1]