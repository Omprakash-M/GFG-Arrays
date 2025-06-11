#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        at=set(a)
        bt=set(b)
        return len(at.union(bt))
