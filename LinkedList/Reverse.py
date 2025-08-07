"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        node = []
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        
        n = len(node)
        for i in range(n//2):
            node[i].data, node[n-i-1].data = node[n-i-1].data, node[i].data
        
        return head