class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_split = merge_and_count(left, right)

            total_inversions = inv_left + inv_right + inv_split
            return merged, total_inversions

        def merge_and_count(left, right):
            i = j = inv_count = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    inv_count += len(left) - i  # All remaining elements in left are inversions

            merged += left[i:]
            merged += right[j:]
            return merged, inv_count

        _, count = merge_sort(arr)
        return count
