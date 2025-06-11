class Solution:
    def missingNum(self, arr):
        temp=set(arr)
        n=max(arr)
        for i in range(1,n+2):
            if i not in temp:
                return i
