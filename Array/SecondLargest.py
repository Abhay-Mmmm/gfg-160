class Solution:
    def getSecondLargest(self, arr):
        seclar = -1
        lar = -1
        for number in arr:
            if number > lar:
                    seclar = lar
                    lar = number
            elif number < lar and number > seclar:
                seclar = number
        
        if seclar != -1:
            return seclar
        else:
            return -1