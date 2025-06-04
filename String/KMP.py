#User function Template for python3

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
        
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        lps = self.computeLPS(pat)
        
        i = j = 0
        result = []
        
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                
            if j == m:
                result.append(i - j)
                j = lps[j-1]
            elif i<n and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return result