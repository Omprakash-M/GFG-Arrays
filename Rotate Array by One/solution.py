#User function Template for python3

class Solution:
    def rotate(self, arr):
        temp=arr.pop()
        arr.insert(0,temp)
        return arr
