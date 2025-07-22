class Solution:    
    def findUnion(self, a, b):
        a_set = set(a)
        b_set = set(b)
        res = list(a_set.union(b_set))
        
        return res