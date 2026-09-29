"""
Problem: Maximum of All Subarrays of Size K
Category: Heaps
Pattern: Monotonic Deque / Max-Heap Sliding Window

Time Complexity:  O(N) using deque / O(N log K) using heap
Space Complexity: O(K) auxiliary space
"""

import heapq


class Solution:
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        ans = []
        heap = []
        # Initialize the heap with the first k elements
        for i in range(k):
            heapq.heappush(heap, (-arr[i], i))
        # The maximum element in the first window
        ans.append(-heap[0][0])
        # Process the remaining elements
        for i in range(k, len(arr)):
            heapq.heappush(heap, (-arr[i], i))
            # Remove elements that are outside the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            # The maximum element in the current window
            ans.append(-heap[0][0])
        return ans


if __name__ == "__main__":
    ob = Solution()
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    print(f"Max of subarrays size {k}: {ob.max_of_subarrays(arr, len(arr), k)}")
