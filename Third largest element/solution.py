class Solution:
    def thirdLargest(self,arr):
        i=1
        while i<=2:
            arr.pop(arr.index(max(arr)))
            i+=1
        return(arr.pop(arr.index(max(arr))))
