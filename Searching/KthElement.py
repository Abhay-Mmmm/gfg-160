class Solution:

    def kthElement(self, a, b, k):
        c = a + b
        c.sort()
        return c[k-1]
