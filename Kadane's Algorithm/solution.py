class Solution:
    def maxSubArraySum(self, arr):
        maxend=arr[0]
        res=arr[0]
        for i in range(1,len(arr)):
            maxend=max(maxend+arr[i],arr[i])
            res=max(maxend,res)
        return res
