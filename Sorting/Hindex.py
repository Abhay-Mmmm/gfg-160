class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i,c in enumerate(citations): #Gives index to i and element to c
            if c >= i+1:
                h = i+1
            else:
                break
            
        return h