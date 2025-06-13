class Solution:
    def maxProduct(self, arr):
        max_so_far = arr[0]
        max_ending_here = arr[0]
        min_ending_here = arr[0]

        for i in range(1, len(arr)):
            num = arr[i]

            if num < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            max_ending_here = max(num, max_ending_here * num)
            min_ending_here = min(num, min_ending_here * num)

            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
